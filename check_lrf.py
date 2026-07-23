import pandas as pd

lrf= pd.read_excel(r"..\Data\april_LRF & VD --LOG SHEET FY2026-2027 (1)(APRIL2026).csv")

print("Rows:", len(lrf))

print("\nColumns:\n")

for col in lrf.columns:
    print(col)