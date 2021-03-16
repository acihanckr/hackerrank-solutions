#start
from collections import Counter

n = int(input())
shoes = Counter(map(int,input().split()))

m = int(input())

total = 0
for _ in range(m):
    line = input().split()
    size = int(line[0])
    price = float(line[1])
    if shoes[size] != 0:
        shoes[size] -= 1
        total += price
print(round(total))
#end