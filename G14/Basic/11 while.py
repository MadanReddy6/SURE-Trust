scores = [3,1,4,7,1,5,9,2,4,2,0,5,6]

i = 1

maximum = scores[0]
minimum = scores[0]

while i < len(scores):
    element = scores[i]
    
    if element > maximum:
        maximum = element

    if element < minimum:
        minimum = element

    i+=1

print(maximum)
print(minimum)