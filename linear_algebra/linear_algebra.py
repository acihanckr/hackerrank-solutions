import numpy as np

#start
n = int(input())
arr = list()
for _ in range(n):
    arr.append([float(k) for k in input().split()])
arr = np.asarray(arr)
print(round(np.linalg.det(arr),2))
#end