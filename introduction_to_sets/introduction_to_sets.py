def average(array):
    #start
    return (sum(set(array)))/(len(set(array)))
    #end

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)