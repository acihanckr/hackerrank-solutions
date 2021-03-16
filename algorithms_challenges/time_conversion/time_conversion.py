#!/bin/python3

import os
import sys
from time import strptime
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #start
    return '{0.tm_hour:02}:{0.tm_min:02}:{0.tm_sec:02}'.format(strptime(s, "%I:%M:%S%p"))
    #end

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
