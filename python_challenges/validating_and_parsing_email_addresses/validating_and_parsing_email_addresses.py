#start
import re

email_format = r'^<[a-zA-Z0-9][a-zA-Z0-9\-_\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'
exp = re.compile(email_format)
n = int(input())
for _ in range(n):
    entry = input().split()
    if exp.match(entry[1]):
        print(' '.join(entry))
#end