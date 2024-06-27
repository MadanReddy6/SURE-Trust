x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8, 7, 7]

# mean
print(round(sum(x)/len(x),2))

# median
x.sort()

half = int(len(x)/2)


if len(x)%2 == 0:
    print((x[half] + x[half - 1])/2)
else:
    print(x[int((len(x)-1)/2)])

# mode

from collections import Counter

counter = {}

for el in x:
    if el in counter:
        counter[el] += 1
    else:
        counter[el] = 1


highest_freq = 0
mode = 0
for el in counter:
    
    if counter[el] > highest_freq:
        highest_freq = counter[el]
        mode = el

print(mode)
