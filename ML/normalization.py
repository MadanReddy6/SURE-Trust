# preprocessing
import pandas as pd

data =pd.read_csv("Concrete.csv")

col = data["superplasticizer"]
col = col - col.mean()
col = col/ col.std()

print(col)