import numpy as np
#start

n,m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = np.array(arr)
print(np.max(np.min(arr, axis = 1)))
#end
