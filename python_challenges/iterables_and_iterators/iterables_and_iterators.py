#start
from itertools import combinations

n = input()
string = input().replace(' ','')
k = int(input())

a_s = sum([1 for i in combinations(range(len(string)),k) if 'a' in [string[i[j]] for j in range(k)]])
total =sum([1 for i in combinations(range(len(string)),k)])
print(a_s/total)
#end