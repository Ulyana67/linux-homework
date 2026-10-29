#!/usr/bin/env python3

def is_valid_dna(dna):
    if dna == "":
        return False

    for nucleotide in dna:
        if nucleotide not in "ATGC":
            return False

    return True


def hamming_distance(s1, s2):
    if not is_valid_dna(s1) or not is_valid_dna(s2):
        return None

    if len(s1) != len(s2):
        return None

    distance = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1

    return distance


print(hamming_distance("ATGC", "CCGC"))
