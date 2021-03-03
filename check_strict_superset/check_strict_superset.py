#start
set_a = set(input().split())
n = int(input())
is_super = True
for _ in range(n):
    set_b = set(input().split())
    if not (set_a>set_b):
        is_super = False
        break
print(is_super)
#end