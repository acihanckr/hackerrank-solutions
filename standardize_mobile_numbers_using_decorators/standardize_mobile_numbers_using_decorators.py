def wrapper(f):
    def fun(l):
        #start
        f([f'+91 {elem[-10:-5]} {elem[-5:]}' for elem in l])
        #end        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


