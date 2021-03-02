#start
from itertools import permutations

read_line = input().split()
r = int(read_line[1])
letters = sorted(read_line[0])

for per in permutations(letters, r):
    print(''.join(per))
#end