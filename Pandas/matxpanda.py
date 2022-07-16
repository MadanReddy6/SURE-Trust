from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv("imdb_top_1000.csv")
data_xy = data[["IMDB_Rating","Gross"]]

data_xy = data_xy.dropna()
data_xy = data_xy.sort_values(by="IMDB_Rating")

x_axis = np.array(data_xy["IMDB_Rating"])
y_axis = np.array(data_xy["Gross"])


for i in range(len(y_axis)):
    el = y_axis[i]
    el = el.replace(",","")
    el = int(el)
    y_axis[i] = el

y_axis = y_axis.astype(np.int32)


plt.plot(x_axis,y_axis,'o')

plt.show()