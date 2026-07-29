import os
import sys
import io
import builtins
import contextlib
import importlib.util

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

get_valid_number = module.get_valid_number
main = module.main


def run_with_mocked_input(func, answers):

    """
    Run `func` with `input()` monkeypatched to return the given answers in
    order, and capture (return value, captured stdout).
    """

    iterator = iter(answers)
    original_input = builtins.input
    builtins.input = lambda prompt='': str(next(iterator))
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            result = func()
    finally:
        builtins.input = original_input
    return result, buffer.getvalue()


# --------------------------------------------------------------------------
# generate evaluation data for get_valid_number: doctest cannot feed stdin
# to a submission on its own, so every testcase first monkeypatches the
# `input` builtin (via a small `_mock_input` helper) before calling the
# function under test. `get_valid_number` both prints (on a retry) and
# returns a value, so a retrying case needs both `+STDOUT` and `+RETURN`:
# with both flags, the doctest judge reads the first line of the expected
# block as the return value and the remaining lines as the expected stdout.
# --------------------------------------------------------------------------

# (answers fed to input(), whether a retry -- and thus printed output -- is
# expected)
gvn_cases = [
    [77],
    [0],
    [1000],
    [-42, 314],
    [1200, 999],
    [-100, 5000, 1],
]

sys.stdout = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf-8')

print(">>> import builtins")
print(">>> def _mock_input(*values):")
print("...     _iterator = iter(values)")
print("...     builtins.input = lambda prompt='': str(next(_iterator))")
print()

for answers in gvn_cases:
    result, stdout = run_with_mocked_input(
        lambda: get_valid_number("Enter number 1: "), answers
    )

    print(f">>> _mock_input({", ".join(str(value) for value in answers)})")
    if stdout:
        print('>>> get_valid_number("Enter number 1: ") # doctest: +STDOUT +RETURN')
        print(result)
        print(stdout, end='')
    else:
        print('>>> get_valid_number("Enter number 1: ")')
        print(result)
    print()

sys.stdout = sys.__stdout__

# --------------------------------------------------------------------------
# generate evaluation data for main(): each case is one full interactive
# session. The list of answers is sized exactly to what a correct solution
# needs to consume -- a submission that (re-)introduces the original bug
# (still asking for the second number after the first turned out invalid)
# runs out of mocked answers and crashes, which the judge reports as a
# runtime error, so those bugs get caught too.
# --------------------------------------------------------------------------

main_cases = [
    [0],                        # x == 0 stops immediately
    [6, 4, 0],                  # one clean multiplication, then stop
    [-5, 250, 999, 0],          # x retried (boundary near 1000), no extra y-prompt
    [3, 1001, 1000, 0],         # y retried, upper boundary 1000 accepted
    [4, 8],                     # dividers -> error, no "Goodbye!"
    [10, 0],                    # y == 0 stops (as opposed to x == 0)
    [2, 9, 5, 7, 0],            # multiple iterations before stopping
]

sys.stdout = open(os.path.join(evaldir, '1.in'), 'w', encoding='utf-8')

print(">>> import builtins")
print(">>> def _mock_input(*values):")
print("...     _iterator = iter(values)")
print("...     builtins.input = lambda prompt='': str(next(_iterator))")
print()

for answers in main_cases:
    _, stdout = run_with_mocked_input(main, answers)

    print(f">>> _mock_input({", ".join(str(value) for value in answers)})")
    print(">>> main() # doctest: +STDOUT")
    print(stdout, end='')
    print()

sys.stdout = sys.__stdout__
