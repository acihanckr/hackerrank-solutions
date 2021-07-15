#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    #start
    counter = 0
    while any([i!=j for i,j in zip(a, sorted(a))]):
        for i in range(n-1):
            if a[i]>a[i+1]:
                hold_my_number = a[i]
                a[i]=a[i+1]
                a[i+1] = hold_my_number
                counter += 1
                break
    
    print(f'Array is sorted in {counter} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    #end