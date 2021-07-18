#!/usr/bin/python3
"""print out the pascal triangle"""

def pascal_triangle(n):
    list1 = []
    if n <= 0:
        return list1
    for i in range(n):
        list2 = []
    for j in range(i + 1):
        if (j == 0) or (j == i) or (j < i):
            list2.append(1)
    else:
        list2.append(list1[i - 1][j] + list1[i - 1][j - 1])
    list1.append(list2)

    return list1
