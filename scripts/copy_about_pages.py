import os
import shutil
from utils.file_traversal import find_directories

# content directory
content_dir = os.path.join('..', 'chapters')

# source files
src_dir = os.path.join(content_dir, '00 prologue', '01 preface')
assert os.path.exists(src_dir), f'missing directory {src_dir!r}'
src_files = ['readme.md', 'about.nl.md', 'about.en.md']
for src_file in src_files:
    src_file = os.path.join(src_dir, src_file)
    assert os.path.exists(src_file), f'missing src file {src_file!r}'

# locate exercise directories
for dest_dir in find_directories(content_dir, mandatory_files=['config.json']):

    # skip directory containing source files
    if dest_dir == src_dir:
        continue

    for src_file in src_files:
        dest_file = os.path.join(dest_dir, src_file)
        src_file = os.path.join(src_dir, src_file)
        # os.symlink(src_file, dest_file)
        shutil.copy(src_file, dest_file)

    print(dest_dir)