#!/usr/bin/python3
"""print out the pascal triangle"""


def pascal_triangle(n):
    list1 = []
    if n > 0:
        for i in range(1, n + 1):
            list2 = []
            C = 1
            for j in range(1, i + 1):
                list2.append(C)
                """use binomial coefficient"""
                C = C * (i - j) // j
            list1.append(list2)
    return list1
