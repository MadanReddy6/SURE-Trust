# corr, conditions
import pandas as pd

dataset = pd.read_csv("./imdb_top_1000.csv")
print(dataset.columns)

dataset = dataset.drop("Poster_Link", axis=1)
# print(dataset.columns)

# print(dataset.info())

avg_val = dataset["Meta_score"].mean()
dataset["Meta_score"] = dataset["Meta_score"].fillna(avg_val)

# if_morethan_80 = (dataset["Meta_score"] > 80)
# print(dataset[["Series_Title","Gross"]][if_morethan_80])

# for i in range(len(if_morethan_80)):
#     if if_morethan_80[i]:
#         print(dataset.loc[i])

# print(dataset.at[966,"Series_Title"])
# print(dataset["Series_Title"][dataset["Year"]>=2000])






