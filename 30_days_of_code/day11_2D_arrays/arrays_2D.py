#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #start
    print(max([sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3]) for i, j in itertools.product(range(0, len(arr)-2), range(0, len(arr[0])-2))]))
    #end