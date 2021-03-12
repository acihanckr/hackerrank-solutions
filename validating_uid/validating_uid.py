#start
import re
n = int(input())

for _ in range(n):
    uid = input()
    if len(set(uid)) != len(uid) or len(uid) != 10:
        print('Invalid')
        continue
    if not (re.match(r'^[a-zA-Z0-9]+$', uid)):
        print('Invalid')
        continue
    if len(re.findall(r'[0-9]', uid))<3:
        print('Invalid')
        continue
    if len(re.findall(r'[A-Z]', uid))<2:
        print('Invalid')
        continue
    print('Valid')
#end