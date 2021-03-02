#start
n = int(input())

calc_list = list()
for _ in range(n):
    calc_list.append(input().split())

for calc in calc_list:
    try:
        print(int(calc[0])//int(calc[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

#end