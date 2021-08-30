import numpy as np

def arrays(arr):
    #start
    return np.array(list(map(float, arr[::-1])))
    #end

arr = input().strip().split(' ')
result = arrays(arr)
print(result)