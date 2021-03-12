import textwrap

def wrap(string, max_width):
    #start
    return '\n'.join(textwrap.wrap(string, max_width))
    #end

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)