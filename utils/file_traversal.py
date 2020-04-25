"""
Helper functions for traversing the problem definitions.
"""

import os
import re

def find_files(
    basedir, 
    name=None, 
    excluded_names=None, 
    isdir=None, 
    isempty=None, 
    atdepth=None
):

    """
    Finds files contained in basedir that meet the following criteria:

        name: specified file name

        excluded_names: file name cannot contain string from this container

        isdir: regular file (False) or directory (True)

        isempty: empty directory (True) or directory containing files (False);
                criteria is only taken into account for directories; it is
                ignored for regular files

        atdepth: specified depth below basedir; file in basedir have depth 0

    Criteria that are not specified, are not taken into account when selecting 
    files.
    """

    if excluded_names is None:
        excluded_names = set()

    assert os.path.isdir(basedir), 'invalid directory: {}'.format(basedir)

    queue = [(basedir, 0)]
    while queue:

        basedir, depth = queue.pop(0)

        for fl in os.listdir(basedir):

            # check if this file is not excluded_names
            exclude_current = False
            for excluded_name in excluded_names:
                if excluded_name in fl:
                    exclude_current = True
                    break
            if exclude_current:
                continue

            # yield file if it matches search conditions
            absolute_name = os.path.join(basedir, fl)
            if (
                # name
                (name is None or re.match(name, fl))
                and
                # atdepth in file hierarchy
                (atdepth is None or atdepth == 0)
                and
                (
                    # no file type restrictions
                    isdir is None
                    or
                    # regular files
                    (isdir == False and os.path.isfile(absolute_name))
                    or
                    # directories
                    (isdir == True and os.path.isdir(absolute_name))
                )
                and
                (
                    # no restrictions on directory content
                    isempty is None
                    or
                    # no directory
                    not os.path.isdir(absolute_name)
                    # content of directory is (not) empty
                    (isempty != bool(len(os.listdir(absolute_name))))
                )
            ):
                yield absolute_name

            # traverse subdirectories
            if (
                os.path.isdir(absolute_name)
                and
                (atdepth is None or depth == atdepth)
            ):
                queue.append((absolute_name, depth + 1))

def find_directories(
    basedir, 
    name=None, 
    excluded_names=None, 
    atdepth=None, 
    mandatory_files=None, 
    mandatory_dirs=None, 
    excluded_files=None, 
    excluded_dirs=None
):

    """
    Finds subdirectories of basedir that meet the following criteria:

        excluded_names: name cannot contain string from this container

        atdepth: specified depth below basedir; basedir itself has depth 0

        mandatory_files: directory must contain all listed mandatory files

        mandatory_dirs: directory must contain all listed mandatory directories

        excluded_files: directory should not contain any of the listed mandatory 
                        files

        excluded_dirs: directory should not contain any of the listed mandatory 
                       directories


    The directories yielded also cannot have a name that contains a string from 
    this container excluded_names. Criteria that are not specified, are not 
    taken into account when searching for a contained file.
    """

    assert os.path.isdir(basedir), 'invalid directory: {}'.format(basedir)

    if excluded_names is None:
        excluded_names = set()

    if mandatory_files is None:
        mandatory_files = set()

    if mandatory_dirs is None:
        mandatory_dirs = set()

    if excluded_files is None:
        excluded_files = set()

    if excluded_dirs is None:
        excluded_dirs = set()

    queue = [(basedir, 0)]
    while queue:

        basedir, depth = queue.pop(0)

        # check if current directory is not in excluded_names
        exclude_dir = False
        for excluded_name in excluded_names:
            if excluded_name in basedir:
                exclude_dir = True
                break
        if exclude_dir:
            continue

        if atdepth is None or depth == atdepth:

            # check if all required regular files are contained
            missing_files = False
            for name in mandatory_files:
                if not os.path.isfile(os.path.join(basedir, name)):
                    missing_files = True
                    break

            # check if all required directories are contained
            missing_dirs = False
            for name in mandatory_dirs:
                if not os.path.isdir(os.path.join(basedir, name)):
                    missing_dirs = True
                    break

            # check if none of the excluded regular files are contained
            spurious_files = False
            for name in excluded_files:
                if os.path.isfile(os.path.join(basedir, name)):
                    spurious_files = True
                    break

            # check if none of the excluded directories are contained
            spurious_dirs = False
            for name in excluded_dirs:
                if os.path.isdir(os.path.join(basedir, name)):
                    spurious_dirs = True
                    break

            if not (missing_files or missing_dirs or spurious_files or spurious_dirs): 
                yield basedir

        if atdepth is None or depth <= atdepth:
            for name in os.listdir(basedir):
                absolute_name = os.path.join(basedir, name)
                if os.path.isdir(absolute_name):
                    queue.append((absolute_name, depth + 1))

# root directory for problem descriptions
problemdir = os.path.join('..', '..', 'opgaven')