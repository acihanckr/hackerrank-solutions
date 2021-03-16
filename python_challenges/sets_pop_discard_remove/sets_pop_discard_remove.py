n = int(input())
s = set(map(int, input().split()))
k = int(input())
#start
for _ in range(k):
    read_line = input().split()
    if read_line[0] == 'pop':
        s.pop()
    elif read_line[0] == 'remove':
        s.remove(int(read_line[1]))
    elif read_line[0] == 'discard':
        s.discard(int(read_line[1]))
print(sum(s))
#end