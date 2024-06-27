import pandas as pd

dataset = pd.read_csv("life_expectancy.csv")[:2500]
print(dataset.shape)
# print(len(dataset))
# print(dataset.columns)

status = pd.get_dummies(dataset["Status"])

dataset = dataset.drop(["Status","Country","Year"], axis=1)
f_dataset = pd.concat([dataset,status],axis=1)

print(f_dataset.head())
# print(pd.get_dummies(status))