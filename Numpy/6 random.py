from numpy import random

# random float numbers
print(random.rand())
print(random.rand(5)*10)
print(random.rand(2,3)*100)

# random interger numbers
print(random.randint(5,10))
print(random.randint(0,101,(2,3)))

# random -1 to +1 float numbers
print(random.randn(5))


