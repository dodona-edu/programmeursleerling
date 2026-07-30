#!/usr/bin/env python3
"""Run the pythia judge on an exercise locally, in Docker.

Usage:

    scripts/verify_pythia_exercise.py <exercise dir> <solution file>

Checks that a solution passes (or fails) an exercise's tests by running the
real judge (https://github.com/dodona-edu/judge-pythia) inside the same Docker
image Dodona uses, so nothing of the judge's comparison logic is reimplemented
here.

The workflow for a new exercise is to run this twice:

  1. with the reference solution, which must pass everything;
  2. with a deliberately wrong solution (add --expect-fail), which must fail
     at least one test.

Exit codes:

    0   the judge ran and the expected outcome was reached
    1   the judge ran and the outcome was not the expected one
    2   infrastructure problem (no Docker, missing image, missing judge
        source, unparseable judge output, not a pythia exercise, the judge
        ran no tests at all, ...) -- says nothing about the solution
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

DEFAULT_IMAGE = 'ghcr.io/dodona-edu/dodona-python:latest'
DEFAULT_JUDGE = os.path.expanduser(
    '~/Documents/Projects/Dodona/judge-pythia'
)

PASSING_STATUS = 'correct answer'

EXIT_OK = 0
EXIT_TESTS_FAILED = 1
EXIT_INFRA = 2


class InfraError(Exception):
    """Something outside the exercise is broken (Docker, image, judge, ...)."""


# --------------------------------------------------------------------------
# config resolution
# --------------------------------------------------------------------------

def repo_root(start):
    """Walk up from `start` until a directory containing .git is found."""
    current = os.path.abspath(start)
    while True:
        if os.path.exists(os.path.join(current, '.git')):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            # no git checkout: fall back to the filesystem root so the
            # dirconfig walk still terminates
            return os.path.abspath(os.sep)
        current = parent


def deep_merge(parent, child):
    """Merge `child` over `parent`, recursing into nested dicts."""
    merged = dict(parent)
    for key, value in child.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def read_json(path):
    try:
        with open(path, encoding='utf-8') as handle:
            return json.load(handle)
    except json.JSONDecodeError as error:
        raise InfraError(f'{path} is not valid JSON: {error}') from error


def resolve_config(exercise_dir):
    """Resolve an exercise's effective config.

    Merges the dirconfig.json files from the repository root down to the
    exercise directory, then the exercise's own config.json on top. Child
    overrides parent, same as Dodona itself does it.
    """
    exercise_dir = os.path.abspath(exercise_dir)
    root = repo_root(exercise_dir)

    # collect the ancestor chain, root first
    chain = []
    current = exercise_dir
    while True:
        chain.append(current)
        if current == root or os.path.dirname(current) == current:
            break
        current = os.path.dirname(current)
    chain.reverse()

    config = {}
    for directory in chain:
        dirconfig = os.path.join(directory, 'dirconfig.json')
        if os.path.isfile(dirconfig):
            config = deep_merge(config, read_json(dirconfig))

    own = os.path.join(exercise_dir, 'config.json')
    if not os.path.isfile(own):
        raise InfraError(
            f'no config.json in {exercise_dir} -- is this an exercise dir?'
        )
    config = deep_merge(config, read_json(own))

    return config


def resolve_judge_mode(config, exercise_dir):
    handler = config.get('evaluation', {}).get('handler')
    if handler is not None and handler != 'pythia':
        raise InfraError(
            f'{exercise_dir} is not a pythia exercise: the resolved config '
            f'sets evaluation.handler to "{handler}" -- use the /verify '
            f'skill for TESTed and SQL exercises'
        )

    mode = config.get('evaluation', {}).get('pythia_judge')
    if not mode:
        raise InfraError(
            f'no evaluation.pythia_judge in the resolved config for '
            f'{exercise_dir} (checked config.json plus every dirconfig.json '
            f'up to the repository root) -- is this a pythia exercise?'
        )
    return mode


# --------------------------------------------------------------------------
# running the judge
# --------------------------------------------------------------------------

def check_infra(judge_dir, image, pull):
    if not shutil.which('docker'):
        raise InfraError('docker not found on PATH')

    probe = subprocess.run(
        ['docker', 'info'], capture_output=True, text=True, check=False
    )
    if probe.returncode != 0:
        raise InfraError(
            'docker is installed but not usable (is the daemon running?):\n'
            + probe.stderr.strip()
        )

    if not os.path.isfile(os.path.join(judge_dir, 'pythia_judge.py')):
        raise InfraError(
            f'no pythia_judge.py in {judge_dir} -- point --judge at a '
            f'checkout of dodona-edu/judge-pythia'
        )

    present = subprocess.run(
        ['docker', 'image', 'inspect', image],
        capture_output=True, text=True, check=False,
    )
    if present.returncode != 0:
        if not pull:
            raise InfraError(
                f'image {image} is not available locally; run '
                f'`docker pull {image}` (or drop --no-pull)'
            )
        print(f'Pulling {image} ...', file=sys.stderr)
        pulled = subprocess.run(
            ['docker', 'pull', '--platform', 'linux/amd64', image],
            check=False,
        )
        if pulled.returncode != 0:
            raise InfraError(f'could not pull {image}')


def make_writable(path):
    """chmod a tree so the container's non-root `runner` user can write."""
    os.chmod(path, 0o777)
    for current, dirnames, filenames in os.walk(path):
        for name in dirnames + filenames:
            target = os.path.join(current, name)
            if not os.path.islink(target):
                os.chmod(target, 0o777)


def run_judge(exercise_dir, solution, mode, judge_dir, image, time_limit):
    """Run the judge in Docker and return (parsed JSON output, stderr)."""
    evaluation = os.path.join(exercise_dir, 'evaluation')
    if not os.path.isdir(evaluation):
        raise InfraError(f'no evaluation/ directory in {exercise_dir}')

    with tempfile.TemporaryDirectory(prefix='pythia-verify-') as scratch:
        workdir = os.path.join(scratch, 'workdir')
        os.makedirs(workdir)

        # exercises may ship files the submission is supposed to find in its
        # working directory (data files, ...), same as judge-pythia's own
        # testing/test.sh does
        source_workdir = os.path.join(exercise_dir, 'workdir')
        if os.path.isdir(source_workdir):
            shutil.copytree(source_workdir, workdir, dirs_exist_ok=True)

        # the container runs as uid 1000 (runner) and has to write in here
        make_writable(scratch)

        config = {
            'resources': '/exercise/evaluation',
            'judge': '/judge',
            'workdir': '/home/runner/workdir',
            'time_limit': time_limit,
            'memory_limit': 100000000,
            'source': '/submission/source.py',
            'pythia_judge': mode,
            'natural_language': 'en',
            'programming_language': 'python',
        }

        command = [
            'docker', 'run', '--rm', '-i',
            '--platform', 'linux/amd64',
            '-v', f'{judge_dir}:/judge:ro',
            '-v', f'{evaluation}:/exercise/evaluation:ro',
            '-v', f'{solution}:/submission/source.py:ro',
            '-v', f'{workdir}:/home/runner/workdir',
            '-w', '/home/runner/workdir',
            image,
            '/judge/run',
        ]

        result = subprocess.run(
            command,
            input=json.dumps(config),
            capture_output=True,
            text=True,
            check=False,
            timeout=time_limit + 120,
        )

    if result.returncode != 0 and not result.stdout.strip():
        raise InfraError(
            'the judge container exited with code '
            f'{result.returncode} and produced no output:\n'
            + (result.stderr.strip() or '(no stderr)')
        )

    try:
        return json.loads(result.stdout), result.stderr
    except json.JSONDecodeError as error:
        raise InfraError(
            f'could not parse the judge output as JSON ({error}).\n'
            f'--- stdout ---\n{result.stdout[:4000]}\n'
            f'--- stderr ---\n{result.stderr[:4000]}'
        ) from error


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

TAG_RE = re.compile(r'<[^>]+>')

ENTITIES = [
    ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'),
    ('&#39;', "'"), ('&nbsp;', ' '), ('&amp;', '&'),
]


def describe(group, fallback):
    """Turn a Dodona description (string or {description, format}) into text."""
    description = group.get('description')
    if isinstance(description, dict):
        description = description.get('description', '')
    if not description:
        return fallback
    description = TAG_RE.sub('', str(description))
    for entity, replacement in ENTITIES:
        description = description.replace(entity, replacement)
    description = ' '.join(description.split())
    return description or fallback


def shorten(value, limit=200):
    value = ' '.join(str(value).split())
    if len(value) > limit:
        value = value[:limit] + ' ...'
    return value


def diff_detail(test):
    """Describe what went wrong in a failing test.

    Most failing tests carry `expected` and `generated`, but the doctest judge
    sometimes reports a line-by-line `data.diff` instead: a list of
    [expected line number, generated line number, expected text, generated
    text, whether the pair matches].
    """
    expected = test.get('expected')
    generated = test.get('generated')

    if expected is None and generated is None:
        rows = test.get('data', {}).get('diff') or []
        mismatches = [row for row in rows if len(row) >= 5 and not row[4]]
        if mismatches:
            return '\n'.join(
                f'line {row[0]}: expected {shorten(row[2], 120)!r}, '
                f'got {shorten(row[3], 120)!r}'
                for row in mismatches[:10]
            )

    if expected is None and generated is None:
        for message in test.get('messages', []):
            text = describe({'description': message.get('description')}, '')
            if text:
                return shorten(text, 300)
        return '(the judge reported no expected/generated values)'

    return (
        f'expected:  {shorten(expected or "")}\n'
        f'generated: {shorten(generated or "")}'
    )


def collect(submission):
    """Flatten the judge's group tree into (depth, label, status, detail)."""
    lines = []
    passed = failed = 0

    levels = ['tab', 'context', 'testcase']

    for tab_index, tab in enumerate(submission.get('groups', [])):
        lines.append((0, f'{levels[0]}: '
                         + describe(tab, f'tab {tab_index + 1}'),
                      tab.get('status'), None))

        for context_index, context in enumerate(tab.get('groups', [])):
            lines.append((1, f'{levels[1]}: '
                             + describe(context, f'context {context_index + 1}'),
                          context.get('status'), None))

            for case_index, case in enumerate(context.get('groups', [])):
                case_status = case.get('status', PASSING_STATUS)
                lines.append((2, f'{levels[2]}: '
                                 + describe(case, f'testcase {case_index + 1}'),
                              case_status, None))

                tests = case.get('tests', [])
                if not tests:
                    # a testcase without explicit tests (e.g. a doctest
                    # statement that only has to run without erroring) still
                    # carries a status of its own, so count that
                    if case_status == PASSING_STATUS:
                        passed += 1
                    else:
                        failed += 1
                    continue

                for test_index, test in enumerate(tests):
                    status = test.get('status', PASSING_STATUS)
                    detail = None
                    if status == PASSING_STATUS:
                        passed += 1
                    else:
                        failed += 1
                        detail = diff_detail(test)
                    lines.append((3, 'test: '
                                     + describe(test, f'test {test_index + 1}'),
                                  status, detail))

    return lines, passed, failed


def report(submission, show_passed):
    """Print the tab/context/testcase/test tree; return (passed, failed)."""
    lines, passed, failed = collect(submission)

    # keep failing lines plus their ancestors; drop the rest unless --all
    keep = [False] * len(lines)
    ancestors = {}
    for index, (depth, _, status, _) in enumerate(lines):
        ancestors[depth] = index
        for deeper in [key for key in ancestors if key > depth]:
            del ancestors[deeper]
        if status not in (None, PASSING_STATUS):
            for held in ancestors.values():
                keep[held] = True

    for index, (depth, label, status, detail) in enumerate(lines):
        if not (show_passed or keep[index]):
            continue
        mark = 'PASS' if status in (None, PASSING_STATUS) else 'FAIL'
        indent = '  ' * depth
        suffix = '' if status in (None, PASSING_STATUS) else f'   [{status}]'
        print(f'{indent}{mark}  {label}{suffix}')
        if detail:
            for line in detail.splitlines():
                print(f'{indent}      {line}')

    return passed, failed


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Run the pythia judge on an exercise in Docker.',
    )
    parser.add_argument('exercise', help='the exercise directory')
    parser.add_argument('solution', help='the .py file to submit')
    parser.add_argument(
        '--judge', default=DEFAULT_JUDGE,
        help=f'checkout of dodona-edu/judge-pythia (default: {DEFAULT_JUDGE})',
    )
    parser.add_argument(
        '--image', default=DEFAULT_IMAGE,
        help=f'judge Docker image (default: {DEFAULT_IMAGE})',
    )
    parser.add_argument(
        '--mode', choices=['doctest', 'output'],
        help='override the pythia_judge mode instead of resolving it',
    )
    parser.add_argument(
        '--time-limit', type=int, default=60,
        help='time limit handed to the judge, in seconds (default: 60)',
    )
    parser.add_argument(
        '--expect-fail', action='store_true',
        help='invert the check: succeed only if the solution is rejected '
             '(for checking a deliberately wrong solution)',
    )
    parser.add_argument(
        '--all', dest='show_passed', action='store_true',
        help='show passing groups too, not just the failing ones',
    )
    parser.add_argument(
        '--no-pull', dest='pull', action='store_false',
        help='do not pull the image if it is missing locally',
    )
    parser.add_argument(
        '--raw', metavar='FILE',
        help="write the judge's raw JSON output to FILE",
    )
    args = parser.parse_args(argv)

    exercise = os.path.abspath(args.exercise)
    solution = os.path.abspath(args.solution)
    judge = os.path.abspath(os.path.expanduser(args.judge))

    try:
        if not os.path.isdir(exercise):
            raise InfraError(f'no such directory: {exercise}')
        if not os.path.isfile(solution):
            raise InfraError(f'no such file: {solution}')

        config = resolve_config(exercise)
        mode = args.mode or resolve_judge_mode(config, exercise)

        check_infra(judge, args.image, args.pull)
        submission, stderr = run_judge(
            exercise, solution, mode, judge, args.image, args.time_limit
        )
    except InfraError as error:
        print(f'INFRASTRUCTURE ERROR: {error}', file=sys.stderr)
        return EXIT_INFRA
    except subprocess.TimeoutExpired:
        print(
            'INFRASTRUCTURE ERROR: the judge container did not finish in time',
            file=sys.stderr,
        )
        return EXIT_INFRA

    if args.raw:
        with open(args.raw, 'w', encoding='utf-8') as handle:
            json.dump(submission, handle, indent=1, sort_keys=True)

    print(f'exercise:   {exercise}')
    print(f'solution:   {solution}')
    print(f'judge mode: {mode}')
    print()

    passed, failed = report(submission, args.show_passed)
    if failed or args.show_passed:
        print()

    accepted = submission.get('accepted', False)
    description = submission.get('description')
    if isinstance(description, dict):
        description = description.get('description', '')

    print(f'{passed} passed, {failed} failed')
    print(f'submission status: {submission.get("status", "?")} '
          f'(accepted: {accepted})')
    if description:
        print(f'judge says: {shorten(describe(submission, ""), 400)}')

    if stderr.strip():
        print()
        print('--- judge stderr ---')
        print(stderr.strip()[:4000])

    if passed == 0 and failed == 0:
        print()
        print(
            'INFRASTRUCTURE ERROR: the judge reported no tests at all, so '
            'nothing can be concluded about this solution -- the '
            'evaluation/ directory may not contain test files for this '
            'judge',
            file=sys.stderr,
        )
        return EXIT_INFRA

    all_good = bool(accepted) and failed == 0

    print()
    if args.expect_fail:
        if all_good:
            print('UNEXPECTED: this solution was accepted, but --expect-fail '
                  'was given, so the tests do not catch this mistake')
            return EXIT_TESTS_FAILED
        print('OK: the solution was rejected, as expected')
        return EXIT_OK

    if all_good:
        print('OK: all tests passed')
        return EXIT_OK
    print('FAILED: the solution was rejected')
    return EXIT_TESTS_FAILED


if __name__ == '__main__':
    sys.exit(main())
