import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)
print(df["PROCESS TIME"].dtype)

print(
    df["PROCESS TIME"]
    .unique()
)
df["PROCESS TIME"] = pd.to_numeric(
    df["PROCESS TIME"],
    errors="coerce"
)

df["Time_Bin"] = pd.cut(
    df["PROCESS TIME"],
    bins=[0,30,45,60,75,1000],
    labels=[
        "0-30",
        "30-45",
        "45-60",
        "60-75",
        "75+"
    ]
)

g11 = (
    df.groupby("Time_Bin")["Total_Al_kg"]
    .mean()
)

plt.figure(figsize=(8,5))

g11.plot(kind="bar")

plt.ylabel("Average Aluminium (kg)")
plt.title("Average Aluminium Consumption vs Process Time")

plt.grid(axis="y")

plt.show()

print(g11)

