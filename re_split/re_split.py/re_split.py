#start
regex_pattern = r"[\,\.]"
#end

import re
print("\n".join(re.split(regex_pattern, input())))