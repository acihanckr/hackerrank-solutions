#this challange can be solve much easier with eval or exec but I wanted to
#write a safer code and parsed the input
#start
from functools import reduce


read_line = input().split()
x = float(read_line[0])
y = float(read_line[1])

replacements = {' ' : '', '**' : '^', '-': '+-'}
pol = input()
pol = reduce(lambda s, kv: s.replace(*kv), replacements.items(), pol).split('+')
result = 0
for term in pol:
    if 'x' not in term:
        result += float(term)
        continue
    term_split = term.split('*')
    if len(term_split) > 1:
        coef = float(term_split[0])
        variable = term_split[1]
    elif term_split[0][0] == '-':
        coef = -1.0
        variable = term_split[0][1:]
    else:
        coef = 1.0
        variable = term_split[0]
    variable_split = variable.split('^')
    result += coef * x**float(variable_split[1]) if len(variable_split)>1 else coef *x
print(result==y)
#end

        
