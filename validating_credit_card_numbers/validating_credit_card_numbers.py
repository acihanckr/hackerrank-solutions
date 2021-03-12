#start
import re
n = int(input())

for i in range(n):
    number = input()
    if not (re.search(r'^[0-9]+$|^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$', number)):
        print('Invalid')
        continue
    elif '-' in number:
        number = ''.join(number.split('-'))
    if not re.search(r'^[4-6]', number):
        print('Invalid')
        
        continue
    if len(number) != 16:
        print('Invalid')
        continue
    if re.search(r'(\d)\1{3,}', number):
        print('Invalid')
        continue
    else:
        print('Valid')
#end