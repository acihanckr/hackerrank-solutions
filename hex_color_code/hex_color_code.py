#start
import re

n = int(input())
text = ''
for _ in range(n):
    line = input()
    text += line + '\n'
regex = r'#[a-fA-F0-9]{3,6}(?!\s\{|\n\{)'

for match in re.findall(regex,text):
    print(match)
#end