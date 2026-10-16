#!/usr/bin/env python3

vvod = int(input())
hours = vvod // 3600
minutes = (vvod % 3600) // 60 
seconds = vvod % 60 
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
