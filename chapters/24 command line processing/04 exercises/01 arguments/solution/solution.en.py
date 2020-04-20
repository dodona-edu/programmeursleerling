#!/usr/bin/env python

import sys

# compute the sum of the arguments
sum = 0
for arg in sys.argv[1:]:
    try:
        sum += int(arg)
    except ValueError:
        print('invalid arguments', file=sys.stderr)
        sys.exit(1)

# output the sum of the arguments
print(sum)
