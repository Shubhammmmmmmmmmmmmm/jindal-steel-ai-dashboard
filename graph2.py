import pandas as pd
import matplotlib.pyplot as plt

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

plt.figure(figsize=(8,5))

plt.scatter(
    master["Final_AL"],
    master["Total_Al_kg"]
)

plt.xlabel("Final Al (%)")
plt.ylabel("Total Aluminium Added (kg)")
plt.title("Final Al vs Aluminium Consumption")

plt.grid(True)

plt.show()