#TODO Try to simplify the code!

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    #start
    time1 = t1.split()
    time1_time = time1[4].split(':')
    
    time2 = t2.split()
    time2_time = time2[4].split(':')
    
    time1_dt = dt.datetime.strptime(f'{time1[3]} {time1[2]} {time1[1]} {time1_time[0]}:{time1_time[1]}:{time1_time[2]}', '%Y %b %d %H:%M:%S')
    time2_dt = dt.datetime.strptime(f'{time2[3]} {time2[2]} {time2[1]} {time2_time[0]}:{time2_time[1]}:{time2_time[2]}', '%Y %b %d %H:%M:%S')
    
    if time1[5][0] == '-':
        print(time1[-1][1:3])
        print(time1[-1][3:])
        print(time1_dt)
        time1_dt = time1_dt + dt.timedelta(hours=int(time1[-1][1:3]), minutes=int(time1[-1][3:]))
        print(time1_dt)
    else:
        print(time1[-1][1:3])
        print(time1[-1][3:])
        print(time1_dt)
        time1_dt = time1_dt - dt.timedelta(hours=int(time1[-1][1:3]), minutes=int(time1[-1][3:]))
        print(time1_dt)

    if time2[5][0] == '-':
        print(time2[-1][1:3])
        print(time2[-1][3:])
        print(time2_dt)
        time2_dt = time2_dt + dt.timedelta(hours=int(time2[-1][1:3]), minutes=int(time2[-1][3:]))
        print(time2_dt)
    else:
        print(time2[-1][1:3])
        print(time2[-1][3:])
        print(time2_dt)
        time2_dt = time2_dt - dt.timedelta(hours=int(time2[-1][1:3]), minutes=int(time2[-1][3:]))
        print(time2_dt)
    result = str(abs(round((time2_dt-time1_dt).total_seconds())))
    return result
    #end



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
