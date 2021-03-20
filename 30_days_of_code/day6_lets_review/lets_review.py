#start
n = int(input())
for _ in range(n):
    string = input()
    print(f'{"".join([c for i, c in enumerate(string) if i%2 ==0])}'
    f' {"".join([c for i, c in enumerate(string) if i%2 != 0])}')
#end