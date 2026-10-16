#!/usr/bin/env python3

import sys


a = sys.argv[1]
c = int(a)

b = bin(c)
o = oct(c)
h = hex(c)

print(f"{c} -> {b} {o} {h}")

bbin = int(b, 2)
ooct = int(o, 8)
hhex = int(h, 16)

print(f"Обратно: {bbin}, {ooct}, {hhex}")
