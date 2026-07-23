import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

top_heats = (
    df.nlargest(
        20,
        "Total_Al_kg"
    )
)

plt.figure(figsize=(12,6))

plt.bar(
    top_heats["HEAT_NO"].astype(str),
    top_heats["Total_Al_kg"]
)

plt.xticks(rotation=90)

plt.ylabel("Total Aluminium (kg)")
plt.xlabel("Heat Number")

plt.title(
    "Top 20 Aluminium Consuming Heats"
)

plt.tight_layout()
plt.show()