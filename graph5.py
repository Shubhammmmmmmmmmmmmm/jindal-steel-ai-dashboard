import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

grade_avg = (
    master.groupby("GRADE")["Total_Al_kg"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(10,6))

grade_avg.plot(kind="bar")

plt.ylabel("Average Aluminium (kg)")
plt.title("Top 15 Aluminium Consuming Grades")

plt.show()