#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from operator import itemgetter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    #start
    lst = {i:0 for i in range(1,6)}
    for ar in arr:
        lst[ar] += 1
    return sorted(lst.items(), key = itemgetter(1), reverse = True)[0][0]
    #end
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().strip().split(' ')))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
