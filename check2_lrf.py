import pandas as pd

xls = pd.ExcelFile(r"..\Data\april_LRF & VD --LOG SHEET FY2026-2027 (1)(APRIL2026).xlsx")

print(xls.sheet_names)