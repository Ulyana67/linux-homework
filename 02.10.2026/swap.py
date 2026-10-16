#!/usr/bin/env python3


a = int(input())
b = int(input())


print(f"До: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")


a, b = b, a
print(f"После 1: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")


a, b = b, a 

c = a
a = b
b = c
print(f"После 2: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")
