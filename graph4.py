import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)
master["PROCESS TIME"] = pd.to_numeric(
    master["PROCESS TIME"],
    errors="coerce"
)
plt.figure(figsize=(8,5))

plt.scatter(
    master["PROCESS TIME"],
    master["Total_Al_kg"]
)
plt.xlabel("Process Time")
plt.ylabel("Total Aluminium Added (kg)")
plt.title("Process Time vs Aluminium Consumption")

plt.grid(True)

plt.show()