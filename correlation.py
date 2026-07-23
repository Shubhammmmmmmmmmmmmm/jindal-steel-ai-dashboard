import pandas as pd

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

corr = master.corr(numeric_only=True)

target_corr = (
    corr["Total_Al_kg"]
    .sort_values(ascending=False)
)

print(target_corr.head(20))