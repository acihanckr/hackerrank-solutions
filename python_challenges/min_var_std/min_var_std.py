import numpy as np
#start

n,m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = np.array(arr)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr, axis = None),11))
#end
