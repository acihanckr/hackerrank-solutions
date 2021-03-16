#start
from itertools import groupby

string  = input()
print(' '.join([f'({sum([1 for i in i[1]])}, {i[0]})' for i in groupby(string)]))
#end