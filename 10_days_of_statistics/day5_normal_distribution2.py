#start
import math

mu, sigma = map(int, input().split())
first_bound = float(input())
second_bound = int(input())

def normal_cumulative(mu: float, sigma: float, bound: float) -> float:
    return 0.5*(1+math.erf((bound - mu)/(sigma*math.sqrt(2))))

print(round(100*(1-normal_cumulative(mu, sigma, first_bound)),2))
print(round(100*(1-normal_cumulative(mu, sigma, second_bound)),2))
print(round(100*normal_cumulative(mu, sigma, second_bound),2))
#end
