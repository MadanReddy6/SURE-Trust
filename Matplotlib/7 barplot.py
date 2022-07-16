from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("./houses.csv")
data = data.dropna()



# for label in labels:
#     print(data["area_type"].value_counts(label))

# print(data.groupby("area_type"))

# for i in data.groupby("area_type"):
#     print(i)

labels = []
values = []

# for i,j in data.groupby("area_type"):
#     labels.append(i)
#     values.append(len(j))

for i,j in data.groupby("area_type"):
    labels.append(i)
    values.append(len(j))

# plt.bar(labels,values)
plt.pie(values,labels=labels,explode=[0,0,0.2,0])

plt.show()
