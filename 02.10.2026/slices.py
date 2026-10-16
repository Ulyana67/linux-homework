#!/usr/bin/env python3

line = input()

length = len(line)

first = line[0]
last = line[-1]


middle = line[len(line) // 2]


second = line[::2]


reverse = line[::-1]


palindrome = (line == reverse)


print(f"Длина: {length}")
print(f"Первый: {first}")
print(f"Последний: {last}")
print(f"Средний: {middle}")
print(f"Каждый второй: {second}")
print(f"Наоборот: {reverse}")
print(f"Палиндром ли: {palindrome}")
