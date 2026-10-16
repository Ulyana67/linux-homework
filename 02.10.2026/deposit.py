#!/usr/bin/env python3


import sys

summ = float(sys.argv[1])
percent = float(sys.argv[2])
years = int(sys.argv[3])

itog = summ * (1 + percent / 100) ** years

print(f"{summ:.0f} {percent:.0f} {years} -> {itog:.2f}")
