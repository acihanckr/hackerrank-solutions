import math
maximum_weight, number_of_boxes, mu, sigma = [float(input()) for _ in range(4)]

def normal_cumulative(mu: float, sigma: float, bound: float) -> float:
    return 0.5*(1+math.erf((bound - mu)/(sigma*math.sqrt(2))))

print(round(normal_cumulative(number_of_boxes*mu,
                sigma*math.sqrt(number_of_boxes), maximum_weight), 4))