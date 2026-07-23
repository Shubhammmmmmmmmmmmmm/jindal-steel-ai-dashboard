import pandas as pd

df = pd.read_excel(r"..\Data\master_dataset_template (1).xlsx")
# print("\nColumns:\n")

# for col in df.columns:
#     print(col)
print(df.info())