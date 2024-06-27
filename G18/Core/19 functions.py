# def add(a,b,c=0,d=0,e=0,f=0):
#     return a+b+c+d+e+f

# print(add(2,9,4,3))


# x = [i for i in range(10)]

# print(x)

import datetime as dt

x = dt.datetime(2002,10,24, 18,34,22)
delta = dt.timedelta(days=3,hours=-5.5)


print(x-delta)