#start
from math import erf,sqrt
mu, sigma = map(float,input().split())

print(round(0.5*(1+erf((float(input())-mu)/(sigma*sqrt(2)))),3))
lower_bound, upper_bound = map(float, input().split())
print(round(0.5*(erf((upper_bound-mu)/(sigma*sqrt(2)))-
    erf((lower_bound-mu)/(sigma*sqrt(2)))),3))
#end