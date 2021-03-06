import numpy as np

#start

n,m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = np.array(arr)
print(np.prod(np.sum(arr, axis = 0)))
#end
