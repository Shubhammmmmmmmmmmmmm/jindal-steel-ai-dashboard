import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)
g14 = (
    df.groupby("GRADE")["Total_Al_kg"]
    .mean()
    .sort_values(ascending=False)
    .head(20)
)

plt.figure(figsize=(12,6))

g14.plot(kind="bar")

plt.ylabel("Average Aluminium (kg)")
plt.title("Top 20 Aluminium Consuming Grades")

plt.grid(axis="y")

plt.xticks(rotation=90)

plt.show()

print(g14)