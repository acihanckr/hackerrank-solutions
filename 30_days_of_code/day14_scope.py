import itertools

class Difference:
    def __init__(self, a):
        self.__elements = a
    #start
    def computeDifference(self):
        self.maximumDifference = max([abs(i-j) for i,j in itertools.combinations(self.__elements,2)] )
    #end

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)