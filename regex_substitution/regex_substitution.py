#start
import re

n = int(input())

for _ in range(n):
    line = input()
    line = re.sub(r'(?<=\s)\|\|(?=\s)', lambda s:'or', line)
    line = re.sub(r'(?<=\s)\&\&(?=\s)', lambda s:'and', line)
    print(line)
#end