def is_leap(year):
    leap = False
    #start
    if year%400==0:
        leap = True
    elif year%100==0:
        leap = False
    elif year%4==0:
        leap = True
    #end    
    return leap

year = int(input())
print(is_leap(year))