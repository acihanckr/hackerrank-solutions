#start

from datetime import date
import calendar

dt = list(map(int, input().split()))
the_day = date(dt[2],dt[0], dt[1])
print(calendar.day_name[the_day.weekday()].upper())


#end