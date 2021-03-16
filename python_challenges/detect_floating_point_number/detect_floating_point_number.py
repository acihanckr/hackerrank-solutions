#start
import re

t = int(input())
exp1 = r'^[\+\-]?\d*\.\d+$'
exp1 = re.compile(exp1)
for _ in range(t):
    result = True if exp1.match(input()) else False
    print(result)
#end