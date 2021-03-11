if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    #start
    print(hash(tuple(integer_list)))
    #end