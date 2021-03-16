#start
from statistics import mean
input()
arr = list(map(float, input().split()))
print((sum([(x-mean(arr))**2 for x in arr])/len(arr))**0.5)
#end
