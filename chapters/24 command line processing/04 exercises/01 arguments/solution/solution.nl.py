#!/usr/bin/env python

import sys

# de som van de argumenten berekenen
som = 0
for arg in sys.argv[1:]:
    try:
        som += int(arg)
    except ValueError:
        print('ongeldige argumenten', file=sys.stderr)
        sys.exit(1)

# de som van de argumenten uitschrijven
print(som)
