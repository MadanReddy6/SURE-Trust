x = [3,6,27,9,21,15,18,33,21,24,30]=

# Updating - insert, append
x.append("hi")
x.insert(-3,"hey")

print(x)
# 33 21
# 21 24

# Deleting - pop, remove
deleted = x.pop(-5)
x.remove("hello")

# print(x[-5])
# print(x[10])
# print(x, deleted)

print(x)