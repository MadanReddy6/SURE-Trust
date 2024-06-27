start = bool(input("Does the week start on Monday? (leave empty for no): "))
print(start)
day = int(input("What day of the week it is? : "))


weekdays = ('mon',"tues","wed","thur","fri","sat","sun")

if start:
    print(weekdays[day-1])
else:
    if day==1:
        print(weekdays[6])
    else:
        print(weekdays[day-2])

