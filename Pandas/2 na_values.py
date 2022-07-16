import pandas as pd

dataset = pd.read_csv("./email.csv",sep=";",index_col = "No",na_values=["_","?","unknown"])


rowise = dataset.dropna(axis=0)
colwise = dataset.dropna(axis=1)


# for col in colwise:
#     for r in rowise[col]:
#         print(r)

dataset["Gender"] = dataset["Gender"].fillna("Prefer Not to say")
dataset["Username"] = dataset["Username"].fillna("____")

dataset = dataset.fillna("Unknown")

# print(dataset.to_string())

# na_values, dropna, fillna

print(dataset["Gender"][3])
# print(dataset.loc[[3,5]][["Username","Gender"]])
print(dataset.iloc[1:4,[2,3,5]].to_string())

# print(dataset.at[3,"Username"])
# print(dataset.iat[3,0])


# print(dataset.to_string())
print(dataset[[True,True,False,True,False]])