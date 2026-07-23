import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

df = master[
    ["Basicity B1", "Total_Al_kg"]
].dropna()

plt.figure(figsize=(8,5))

plt.scatter(
    df["Basicity B1"],
    df["Total_Al_kg"]
)

plt.xlabel("Basicity B1")
plt.ylabel("Total Aluminium Added (kg)")
plt.title("Basicity vs Aluminium Consumption")

plt.grid(True)

plt.show()
