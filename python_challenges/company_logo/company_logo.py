#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    #start
    counter = Counter(s)
    most_common = sorted((set(counter.values())), reverse = True)[0:3]
    complete_list = []
    for i in range(len(most_common)):
        commons = {k:v for k, v in counter.items() if v == most_common[i]}
        for key in sorted(commons.keys()):
            complete_list.append([key, commons[key]])
        
    for i in complete_list[0:3]:
        print(i[0]+' '+str(i[1]))
    #end