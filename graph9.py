import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

df = master[
    ["Final_N2", "Total_Al_kg"]
].dropna()

plt.figure(figsize=(8,5))

plt.scatter(
    df["Final_N2"],
    df["Total_Al_kg"]
)

plt.xlabel("Final N2 (ppm)")
plt.ylabel("Total Aluminium Added (kg)")
plt.title("Final N2 vs Aluminium Consumption")

plt.grid(True)

plt.show()