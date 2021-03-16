if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#start
print(sorted(list(set(arr)), reverse = True)[1])
#end