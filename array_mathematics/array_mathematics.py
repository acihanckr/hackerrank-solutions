import numpy as np

#start
n, m = map(int, input().split())
arr1 = list()
arr2 = list()
for _ in range(n):
    arr1.append(list(map(int,input().split())))
for _ in range(n):
    arr2.append(list(map(int,input().split())))
arr1 = np.array(arr1)
arr2 = np.array(arr2)
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.floor_divide(arr1,arr2))
print(np.mod(arr1,arr2))
print(np.power(arr1,arr2))
#end
