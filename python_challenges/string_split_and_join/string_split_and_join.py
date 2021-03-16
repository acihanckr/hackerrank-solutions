def split_and_join(line):
    #start
    return '-'.join(line.split())
    #end

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)