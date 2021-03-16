#start
from itertools import combinations_with_replacement

read_line = input().split()
r = int(read_line[1])
letters = sorted(read_line[0])

for per in combinations_with_replacement(letters, r):
    print(''.join(per))
#end