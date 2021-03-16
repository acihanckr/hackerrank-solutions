#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the solve function below.
def solve(string):
    #start
    return reduce(lambda t, s: t.replace(s, s.capitalize()), set(string.split()), string)
    #end
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
