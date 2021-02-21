#start
from collections import defaultdict

n,m = map(int,input().split())

a = []
b = []
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

aList = defaultdict(list)
for i, element in enumerate(a):
    aList[element].append(i+1)

for element in b:
    if len(aList[element]) == 0:
        print(-1)
    else:
        print(' '.join(map(str,aList[element])))
#end