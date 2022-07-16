from matplotlib import pyplot as plt
import pandas as pd

# data = pd.read_csv("./houses.csv")
# data = data.dropna(axis=0)

higher = 0
lower = 0
# avg = data["price"].mean()
import numpy as np

values = np.array([31,5,22,25,1,83,5,47,12,49,6,50])
avg = values.mean() 

for i in values:
    if i > avg:
        higher += 1
    else:
        lower += 1

# for i in data["price"]:
#     if i > avg:
#         higher += 1
#     else:
#         lower += 1


# plt.pie([higher,lower],labels=["Expensive","Cheap"], colors=["red","green"], explode = [0.3,0])

# first we pass in the list of values we want to compare, then the labels of those values
# explode means how out of the pie a part is gonna be
plt.pie([higher,lower],labels=["Greater","Lesser"], colors=["red","green"], explode = [0.3,0])

plt.show()