#start
t = int(input())

for _ in range(t):
    input()
    set_a = set(input().split())
    input()
    set_b = set(input().split())
    print(set_a.issubset(set_b))
    
#end