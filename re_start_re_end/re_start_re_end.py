#start
import re

s = input()
k = input()

if re.findall('(?='+k+')',s):
    for item in re.finditer('(?='+k+')',s):
        print(f'({item.start()}, {item.start()+len(k)-1})')
else:
    print('(-1, -1)')
#end