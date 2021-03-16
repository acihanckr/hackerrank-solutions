#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #start
    print(f'{sum([a>0 for a in arr])/len(arr):.5f}')
    print(f'{sum([a<0 for a in arr])/len(arr):.5f}')
    print(f'{sum([a==0 for a in arr])/len(arr):.5f}')
    #end
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
