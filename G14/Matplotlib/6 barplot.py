from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("./Matplotlib/economy.csv")
data = data.dropna()

years = data["Year"]
gdp = data["GDP per capita"]



names = ["Aman","Ashu","Anky","Ansh"]
heights = [167, 180, 177, 152]

plt.title("Height Graph")
plt.xlabel("Names")
plt.ylabel("Height(in cms)")

# first we need to pass in the labes
# then the gap between the bars
plt.bar(names, heights, 0.5, color=["red","green"])

plt.show()
