#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #start
    print(min([sum(items) for items in combinations(arr,len(arr)-1)]), 
                max([sum(items) for items in combinations(arr,len(arr)-1)]))
    #end
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
