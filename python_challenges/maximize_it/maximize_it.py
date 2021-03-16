#start
from itertools import product

first_line = input().split()
k = int(first_line[0])
m = int(first_line[1])
smax = 0
list_of_lists = []
for _ in range(k):
    list_of_lists.append(list(map(int, input().split()))[1:])
for elements in product(*list_of_lists):
    smax = max(smax, sum(map(lambda x: x**2, elements))%m)
print(smax)
#end
