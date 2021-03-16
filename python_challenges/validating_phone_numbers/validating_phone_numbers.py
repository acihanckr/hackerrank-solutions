#start
import re

n = int(input())
exp = r'^[789]\d{9}$'
exp = re.compile(exp)
for _ in range(n):
    print('YES' if exp.match(input()) else 'NO')
#end