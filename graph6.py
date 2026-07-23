import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

df = master[
    ["FeO (in slag)", "Total_Al_kg"]
].dropna()

plt.figure(figsize=(8,5))

plt.scatter(
    df["FeO (in slag)"],
    df["Total_Al_kg"]
)

plt.xlabel("FeO in Slag (%)")
plt.ylabel("Total Aluminium Added (kg)")
plt.title("FeO in Slag vs Aluminium Consumption")

plt.grid(True)

plt.show()