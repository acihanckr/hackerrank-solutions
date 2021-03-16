#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    #start
    total = round(meal_cost+(tax_percent*meal_cost/100)+(tip_percent*meal_cost/100))
    print(total)
    return total
    #end
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
