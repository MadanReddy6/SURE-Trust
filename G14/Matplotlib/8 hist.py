from matplotlib import pyplot as plt
import pandas as pd

# data = pd.read_csv("../houses.csv")
# data = data.dropna(axis=0)

# x = data["total_sqft"]

x = [2,1,4,5,7,9,2,3,3,6,8,4,12]

plt.title("Figure 7")
# here bins parameter decides how many particions are we gonna do of our histogram
plt.hist(x,bins=4)
# now as the max value in x is 12, and bins is 4, so the 4 bars will display the frequencies from 1-3,4-6,7-9,10-12
plt.show()
