#TODO adjust using correct quantile defition
#start
from statistics import median

input()
arr = list(map(int, input().split()))
med = median(arr)
first_half = [c for c in arr if c<med]
second_half = [c for c in arr if c>med]
print(round(median(first_half)))
print(round(med))
print(round(median(second_half)))
#end
