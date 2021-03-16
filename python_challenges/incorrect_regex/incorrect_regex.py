#start

import re

t = int(input())

for _ in range(t):
    line = input()
    is_valid = True
    try:
        re.compile(line)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
    
#end