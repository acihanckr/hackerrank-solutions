def merge_the_tools(string, k):
    #start
    for i in range(len(string)//k):
        chs = [c for c in string[i*k:(i+1)*k]]
        output = ''
        for c in chs:
            if c not in output:
                output += c
        print(output)
    #end

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)