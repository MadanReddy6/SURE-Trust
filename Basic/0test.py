x = [3,1,5,2,3,1]
x.sort()

print(x)
if len(x)%2 == 1:
    mid = (len(x)-1)//2
    median = x[mid]
else:
    mid1 = len(x)//2
    mid2 = mid1 - 1

    median = (x[mid1] + x[mid2])/2

print(median)