import pandas as pd

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

print("Rows, Columns")
print(master.shape)

print("\nMissing Values")
print(
    master.isna()
    .sum()
    .sort_values(ascending=False)
    .head(20)
)

print("\nNumerical Summary")
print(
    master.describe()
)