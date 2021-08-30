#start
input()
numbers = map(int, input().split())
print(any([n == n[::-1] for n in numbers]) and all([n>0 for n in numbers]))
#end