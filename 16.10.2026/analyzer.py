#!/usr/bin/env python3



sequences = []

while True:
    dna = input()

    if dna == "STOP":
        break

    valid = True

    for nucleotide in dna:
        if nucleotide not in "ATGC":
            valid = False
            break

    if valid and dna != "":
        sequences.append(dna)
    else:
        print("Предупреждение: неправильная последовательность ДНК")

print(len(sequences))

lengths = []

for dna in sequences:
    lengths.append(len(dna))

print(lengths)
