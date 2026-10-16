#!/usr/bin/env python3

vvod = input()
summ = 0 
for i in vvod:
	summ += int(i)

reverse = vvod[::-1]

print(f'{summ}, {reverse}')
