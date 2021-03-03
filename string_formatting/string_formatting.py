def print_formatted(number):
    # start
    for i in range(1,number+1):
        n = len(bin(number).lstrip("0b"))
        print(f'{str(i):>{n}} {oct(i).lstrip("0o"):>{n}} {hex(i).lstrip("0x").upper():>{n}} {bin(i).lstrip("0b"):>{n}}')
    #end

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)