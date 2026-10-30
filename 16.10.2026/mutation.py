#!/usr/bin/env python3


reference = input()
sample = input()

for i, nucleotide in enumerate(reference):
    if nucleotide != sample[i]:
        print(f"{i + 1}: {nucleotide} > {sample[i]}")

