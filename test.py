import pandas as pd

df = pd.read_excel(r"..\Data\master_dataset_template (1).xlsx")
print(df.head())
df.columns
df.head()
df.to_excel(r"..\Data\master_dataset_template (1).xlsx", index=False)
