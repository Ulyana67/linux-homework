#!/usr/bin/env python3

expression = [2.5, 7.1, 0.8, 5.4, 9.2, 3.0]

def filter_expression(values, threshold=5.0):
    result = []
    for value in values:
        if value > threshold:
            result.append(value)
    return result

print(filter_expression(expression))
