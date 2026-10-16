#!/usr/bin/env python3

s = input()

letters = ['G', 'C']
nums = [0, 0]

for x in s:
    for i in range(2):
        if x == letters[i]:
            nums[i] += 1

gc = (nums[0] + nums[1]) / len(s) * 100

print(f"{gc:.2f}%")
