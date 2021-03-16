import numpy as np

#start
n = int(input())
arr1 = list()
arr2 = list()
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(n):
    arr2.append(list(map(int, input().split())))
arr1 = np.array(arr1)
arr2 = np.array(arr2)
print(np.dot(arr1, arr2))
#end
