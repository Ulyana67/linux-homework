#!/usr/bin/env python3




sequences = [
    "AACG",
    "AATG",
    "TATG",
    "TTTG"
]

for i in range(len(sequences)):
    for j in range(len(sequences)):
        distance = 0

        for k in range(len(sequences[i])):
            if sequences[i][k] != sequences[j][k]:
                distance += 1

        print(distance, end=" ")
    print() 
