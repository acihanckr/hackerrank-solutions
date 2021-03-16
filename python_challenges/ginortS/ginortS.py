#start
import re

string = input()
odd_digits = [c for c in string if c in '13579']
even_digits = [c for c in string if c in '02468']
letters = re.findall(r'\d',string)
upper_letters = re.findall(r'[A-Z]',string)
lower_letters = re.findall(r'[a-z]',string)
print(''.join(sorted(lower_letters)+sorted(upper_letters)+sorted(odd_digits)+sorted(even_digits)))
#end