#start
from itertools import combinations

read_line = input().split()
r = int(read_line[1])
letters = sorted(read_line[0])

for i in range(1,r+1):
    for per in combinations(letters, i):
        print(''.join(per))
#end