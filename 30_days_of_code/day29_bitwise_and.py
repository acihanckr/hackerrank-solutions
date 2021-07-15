#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    #start
    if K%2==1:
        return K-1
    else:
        if all(a&b != K-1 for a,b in itertools.combinations(range(N,K-2,-1),2)):
            return K-2
        else:
            return K-1
    #end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
