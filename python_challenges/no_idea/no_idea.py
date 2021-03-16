#start
from collections import Counter
input()
arr = input().split()
a_arr = set(input().split())
b_arr = set(input().split())

a_arr = a_arr.difference(b_arr)
b_arr = b_arr.difference(a_arr)

happi = 0 
for k in arr:
    if k in a_arr:
        happi += 1
    elif k in b_arr:
        happi -= 1
print(happi)
#end