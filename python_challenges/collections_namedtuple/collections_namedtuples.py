#start
#the code is a little more crowded than I'd like but one question in the
#challange was 'Can you solve this challenge in 4 lines of code or less?'
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
print(sum([float(Student(*input().split()).MARKS) for _ in range(n)])/n)
#end