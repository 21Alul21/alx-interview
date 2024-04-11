#!/usr/bin/python3
""" this module contains the solution
to the paschal triangle using python,
the paschal triangle is formed based on the
number of input rows n
"""

def pascal_triangle(n):
    """ paschal triangle function """

    if n <= 0:
        return []
    pc = []
    for i in range(n):
        inner = []
        if len(pc) == 0:
            pc.append([1])
            continue
        else:
            new = [0] + pc[-1] + [0]
            count = 0
            for j in range(len(new) - 1):
                val = new[count] + new[count + 1]
                inner.append(val)
                count += 1
        pc.append(inner)

    return pc
