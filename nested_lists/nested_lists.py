#start
students_list = list()
grades = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    students_list.append([name, score])
    grades.add(score)
        
for name in sorted([student[0] for student in students_list if student[1]==sorted(list(grades))[1]]):
    print(name)
#end