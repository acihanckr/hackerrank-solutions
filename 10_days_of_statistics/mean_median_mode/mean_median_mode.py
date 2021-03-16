#start
import numpy as np
from scipy import stats

input()
arr = np.array(list(map(float, input().split())))
print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr)[0][0])
#end
