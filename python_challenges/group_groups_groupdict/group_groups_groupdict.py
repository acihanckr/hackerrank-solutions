#start
import re

reg = re.match(r'.*?([^_\W])\1', input())
if reg:
    print(reg.group(1))
else:
    print(-1)
#end