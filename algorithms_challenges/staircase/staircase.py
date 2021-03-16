#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #start
    print('\n'.join([('#'*i).rjust(n) for i in range(1,n+1)]))
    #end
if __name__ == '__main__':
    n = int(input())

    staircase(n)
