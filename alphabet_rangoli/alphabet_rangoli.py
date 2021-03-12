import string
def print_rangoli(size):
    #start
    for j in range(n):
        letter_list = [c for c in string.ascii_lowercase[n-1:n-j-1:-1]]\
                         + [c for c in string.ascii_lowercase[n-j-1:n]]
        print('-'.join(letter_list).center(4*n-3,'-'))
        
    for j in range(n-2,-1,-1):
        letter_list = [c for c in string.ascii_lowercase[n-1:n-j-1:-1]]\
                         + [c for c in string.ascii_lowercase[n-j-1:n]]
        print('-'.join(letter_list).center(4*n-3,'-'))
    #end
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)