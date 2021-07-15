#start
import math
n = int(input())
for _ in range(n):
    m = int(input())
    is_prime = True if m!=1 else False
    for i in range(2, int(math.sqrt(m)+1)):
        if m%i==0: 
            is_prime = False
    print('Prime' if is_prime else 'Not prime')
#end
