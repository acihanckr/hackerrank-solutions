#start
from itertools import product

a = input().split()
b = input().split()

tuples = []
for a,b in product(a,b):
    tuples.append((a,b))
print(' '.join(map(lambda x: f'({x[0]}, {x[1]})', tuples)))
#end