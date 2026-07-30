#!/usr/bin/env python

import sys

for arg in sys.argv[1:]:
    try:
        int(arg)
    except ValueError:
        print('ongeldige argumenten', file=sys.stderr)
        sys.exit(1)
