#start

input()
set_a = set(map(int,input().split()))
input()
set_b = set(map(int,input().split()))

sym_diff = set_a.difference(set_b).union(set_b.difference(set_a))
for number in sorted(list(sym_diff)):
    print(number)

#end