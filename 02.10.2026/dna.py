#!/usr/bin/env python3

import sys

dna = sys.argv[1]

rna = dna.replace('T', 'U')

a = str.maketrans('ATGC', 'TACG')
c = dna.translate(a)

reverse = c[::-1]


codon = dna.find('ATG')

print(f"{dna} -> {rna}, {reverse}, {codon}")
