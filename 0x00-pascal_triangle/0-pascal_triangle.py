#!/usr/bin/env python3
from typing import List


def paschal_triangle(n: int) -> List[List[int]]:
    """ paschal triangle function """

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
