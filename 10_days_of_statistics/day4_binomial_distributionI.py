# start
# from scipy.stats import binom
import math

probs = input().split()
p = float(probs[0])/(float(probs[0])+float(probs[1]))

for i in range(3):
    comp_prob += math.factorial(6)/(math.factorial(6-i)*math.factorial(i))* p**i*(1-p)**(6-i)
print(round(1- comp_prob,3))


# print(1-binom.cdf(2, 6, p))
#end