import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

cols = [
    "Total_Al_kg",
    "Initial_AL",
    "Final_AL",
    "Initial_N2",
    "Final_N2",
    "LIFTING TEMERATURE",
    "PROCESS TIME",
    "POWER_y",
    "HM",
    "DRI",
    "LIME_y",
    "DOLO"
]

corr = (
    master[cols]
    .corr(numeric_only=True)
)

plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title(
    "Correlation Matrix of Aluminium Consumption Variables"
)

plt.show()