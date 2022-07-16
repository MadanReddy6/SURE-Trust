# import pandas as pd

# data=pd.read_csv("imdb_top_1000.csv")

# # print(data)

# count = 0

# for i in range(len(data)):
#     row = data.loc[i]

#     # if "Action" in row["Genre"]:
#     #     print(row["Series_Title"])

#     track = True
#     for j in row:
#         if str(j) == "nan":
#             track = False
#             break
    
#     if track:
#         # count+=1
#         print(row)

# print(count)