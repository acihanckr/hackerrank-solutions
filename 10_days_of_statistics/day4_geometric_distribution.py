#start
line = input().split()
p = float(line[0])/float(line[1])
k = int(input())

print(round((1-p)**(k-1)*p,3))
#end