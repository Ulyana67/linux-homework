#!/usr/bin/env python3

s = input()

letters = ['A', 'T', 'C', 'G']
comp = ['T', 'A', 'G', 'C']
ans = []

for x in s:
    for i in range(4):
        if x == letters[i]:
            ans.append(comp[i])

ans.reverse()

print(''.join(ans))
