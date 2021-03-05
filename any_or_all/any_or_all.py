#start
input()
numbers = input().split()
print(any([n == n[::-1] for n in numbers]) and all([int(n)>0 for n in numbers]))
#end