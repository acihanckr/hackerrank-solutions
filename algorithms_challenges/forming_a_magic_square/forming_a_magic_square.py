#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from itertools import permutations

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    #start
    def is_perfect(arr):
        if (sum(arr[:3]) == 15 and sum(arr[3:6]) == 15 and
                sum(arr[::3]) ==15 and sum(arr[1::3]) ==15 and
                sum(arr[::4]) == 15 and sum(arr[2:7:2]) == 15):
                return True
    s = reduce(lambda a,b: a+b,s)
    perfects = [arr for arr in permutations(range(1,10)) if is_perfect(arr)]
    return min([sum([abs(a-b) for a,b in zip(perfect,s)]) for perfect in perfects])
    #end
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
