#!/usr/bin/env python3



rna = input()

stop_codons = ["UAA", "UAG", "UGA"]
count = 0
stop_codon = ""

for i in range(0, len(rna) - 2, 3):
    codon = rna[i:i + 3]

    if codon in stop_codons:
        stop_codon = codon
        break

    count += 1

print(f"Количество кодирующих кодонов: {count}")
print(f"Стоп-кодон: {stop_codon}")
