import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)
df["HM"] = pd.to_numeric(
    df["HM"],
    errors="coerce"
)

df["HM_Bin"] = pd.cut(
    df["HM"],
    bins=[0,40,50,60,70,100]
)

g13 = (
    df.groupby("HM_Bin")["Total_Al_kg"]
    .mean()
)

plt.figure(figsize=(8,5))

g13.plot(kind="bar")

plt.ylabel("Average Aluminium (kg)")
plt.title("Hot Metal (%) vs Aluminium Consumption")

plt.grid(axis="y")

plt.show()

print(g13)

print(df[["HM","Total_Al_kg"]].corr())