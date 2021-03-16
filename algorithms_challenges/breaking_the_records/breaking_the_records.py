#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    #start
    max_count = 0
    min_count = 0
    for ndx, score in enumerate(scores):
        if ndx == 0:
            continue
        if score > max(scores[:ndx]):
            max_count += 1
        if score < min(scores[:ndx]):
            min_count += 1
    return max_count, min_count
    #end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
