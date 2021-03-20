#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    #start
    print(max([len(s) for s in re.findall(r'1+', bin(n))]))
    #end
