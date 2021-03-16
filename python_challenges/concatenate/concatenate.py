import numpy as np

#start
n,m,p = map(int, input().split())
first_list = list()
second_list = list()

for _ in range(n):
    first_list.append(list(map(int,input().split())))
for _ in range(m):
    second_list.append(list(map(int,input().split())))
arr1 = np.array(first_list)
arr2 = np.array(second_list)
print(np.concatenate((arr1,arr2)))
#end