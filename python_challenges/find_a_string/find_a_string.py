import re

def count_substring(string, sub_string):
    #start
    return len(re.findall(rf'(?={sub_string})', string))
    #end

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)