#start
import re

s = input()
if re.findall(r'(?<=[^aeiouAEIOU\W_])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU\W_])',s):
    for subs in re.finditer(r'(?<=[^aeiouAEIOU\W_])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU\W_])',s):
        print(subs.group(1))
else:
    print(-1)
#end