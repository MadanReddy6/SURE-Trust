# two = {2,4,6,8,10,12,14,16,18,20,22,24}
three = {3,6,9,12,15,18,21,24,27,30}
four = {4,8,12,16,20,24,28,32,36,40}
five = {5,10,15,20,25,30,35,40,45,50}

# six = two.intersection(three)

# print(len(six))
# print(len(two))
# print(len(three))

# print(two.union(three))

# print(two.difference(three))
# print(three.difference(two))


# make a set for the table of 3
# add the set for table of 5 in the table of 4
new_set = four.union(five)

# then print out the length of the common elements in the 2 sets
# print(len(new_set.intersection(three)))

# then find out the values for the image
new_set2 = new_set.union(three)
common = new_set.intersection(three)

print(new_set2.difference(common))
print(new_set.symmetric_difference(three))


# find out the values unique to the second set 
# print(three.difference(new_set))