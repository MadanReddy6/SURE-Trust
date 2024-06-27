from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("./Matplotlib/economy.csv")
data = data.dropna()

years = data["Year"]
gdp = data["GDP per capita"]
debt = data["Government debt( of GDP)"]
# print(years,gdp)

plt.subplot(1,2,1)
plt.plot(years, gdp,marker="o",color="#282a36")
plt.xlabel("Years")
plt.ylabel("GDP/capita")

plt.subplot(1,2,2)
plt.plot(years, debt, color='red')
plt.xlabel("Years")
plt.ylabel("Gov Debt")

plt.show()
# print(data)

