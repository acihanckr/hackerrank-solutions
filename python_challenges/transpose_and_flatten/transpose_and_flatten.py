import numpy as np

#start
n,m = map(int,input().split())
list_of_lists = list()
for _ in range(n):
    list_of_lists.append(list(map(int,input().split())))
arr = np.array(list_of_lists)
print(arr.transpose())
print(arr.flatten())
#end