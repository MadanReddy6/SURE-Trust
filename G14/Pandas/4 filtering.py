import pandas as pd

dataset = pd.read_csv("./imdb_top_1000.csv")
# print(dataset.columns)
dataset = dataset.drop(["Poster_Link","Overview"], axis=1)
# print(dataset.columns)
# dataset = dataset.drop([1,2,3,10,100], axis=0)
# print(len(dataset))

# print(dataset["Series_Title"][dataset["Overview"].str.contains("murderer")])
# print(dataset[dataset["Genre"].str.contains("Action")])

# print(dataset[dataset["Series_Title"].str.startswith("The")])
# print(dataset["Star1"][dataset["Star1"].str.startswith("T")])

# print(len(dataset[(dataset["Certificate"] == "R")]))
# print(len(dataset[(dataset["Certificate"] == "U")]))

# print(dataset[(dataset["Certificate"] == "R") | (dataset["Certificate"] == "U")])
# and = "&"
# or = "|"

# print(dataset["Genre"][(dataset["Genre"] == "Drama") | (dataset["Genre"].str.contains("Romance"))])

# print(dataset.sort_values(by="Series_Title").to_string())

dataset = dataset.sort_values(by="Year")
print(dataset)

print(dataset.loc[321])
print(dataset.iloc[321])




# str.lower
# add_prefix
# astype
# apply