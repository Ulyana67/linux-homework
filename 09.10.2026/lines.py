#!/usr/bin/env python3

letters = input().split()
n = int(input())

words = ['']

for i in range(n):
    new_words = []
    for word in words:
        for x in letters:
            new_words.append(word + x)
    words = new_words

for word in words:
    print(word)
