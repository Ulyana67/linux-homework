#!/usr/bin/env python3

s = input()

letters = ['A', 'C', 'G', 'T']
nums = [0, 0, 0, 0]

for x in s:
    for i in range(4):
        if x == letters[i]:
            nums[i] += 1

print(*nums)
