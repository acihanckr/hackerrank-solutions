#start
import math

inps = input().split()
p = float(inps[0])/100
n = int(inps[1])

def binomial_cdf(k, n, p):
    prob = 0
    for i in range(k):
        prob += math.factorial(n)/(math.factorial(n-i)*math.factorial(i))* p**i*(1-p)**(n-i)
    return prob
    

print(round(binomial_cdf(3,n,p),3))
print(round(1 - binomial_cdf(2,n,p),3))
#end