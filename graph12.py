import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)
df["FinalAl_Bin"] = pd.cut(
    df["Final_AL"],
    bins=[0,0.02,0.03,0.04,0.05,0.10,1.5]
)

g12 = (
    df.groupby("FinalAl_Bin")["Total_Al_kg"]
    .mean()
)

plt.figure(figsize=(8,5))

g12.plot(kind="bar")

plt.ylabel("Average Aluminium (kg)")
plt.title("Final Al Target vs Aluminium Consumption")

plt.grid(axis="y")

plt.show()

print(g12)