from functools import reduce

cube = lambda x: x**3

def fibonacci(n):
    #start
    if n == 0:
        return list()
    elif n== 1:
        return [0]
    else:
        return reduce(lambda s, i: s + [s[-1]+s[-2]], range(n-2),[0,1])
    #end

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))