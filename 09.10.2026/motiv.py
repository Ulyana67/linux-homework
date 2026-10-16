#!/usr/bin/env python3

s = input()
t = input()

pos = []

for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
        pos.append(i + 1)

print(*pos)
