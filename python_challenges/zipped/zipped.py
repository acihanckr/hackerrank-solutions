#start
read_line = input().split()
n = int(read_line[0])
x = int(read_line[1])
grades = list()
for _ in range(x):
    grades.append(list(map(float, input().split())))
for grade in zip(*grades):
    print(sum(grade)/x)
#end