#start
difference = [time1-time2 for time1, time2 in zip(map(int,input().split()),map(int,input().split()))]
if difference[2]<0:
    print(0)
elif difference[2]>0:
    print(10000) 
elif difference[1]<0:
    print(0)
elif difference[1]>0:
    print(difference[1]*500)
elif difference[0]>0:
    print(difference[0]*15)
else:
    print(0)
#end