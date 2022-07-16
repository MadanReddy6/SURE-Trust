import pandas as pd

# data = pd.read_csv("./Pandas/houses.csv")
# data = pd.read_csv("./Pandas/email.csv",sep=";")

# data = pd.read_csv("./Pandas/own.csv",sep="|")

# data = pd.read_csv("./Pandas/own.csv",sep="|",index_col="name")



data = pd.read_csv("./Pandas/email.csv",sep=";",index_col="No")

print(data)


print(data["Last name"])
print(data.loc[1])


print(data[["First name","Last name"]])