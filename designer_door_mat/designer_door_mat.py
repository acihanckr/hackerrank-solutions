#start
n, m = map(int, input().split())
dim1 = n//2
dim2 = m//2
for i in range(dim1):
    print(''.join(['.|.']*(2*i+1)).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(dim1,0,-1):
    print(''.join(['.|.']*(2*i-1)).center(m,'-'))
#end