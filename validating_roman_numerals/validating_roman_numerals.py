regex_pattern = r'^M{,3}(CM|D?(C{,3})|CD)?(XC|L?(X{,3})|XL)?(IX|V?(I{,3})|IV)?$'
#start - regex added - end#

import re
print(str(bool(re.match(regex_pattern, input()))))