import pandas as pd

eaf = pd.read_excel(r"..\Data\EAF heat details.xlsx")

print("Rows:", len(eaf))

# for col in eaf.columns:
#     print(repr(col))

import pandas as pd

eaf = pd.read_excel(r"..\Data\EAF heat details.xlsx")

keep_cols = [
    'Date',
    'H NO.',
    'HM',
    'DRI',
    'LIME',
    'DOLO',
    'CPC',
    'POWER',
    'OXY',
    'POT',
    'AT',
    'T WT',
    'Production',
    'YIELD'
]

eaf_clean = eaf[keep_cols]

print(eaf_clean.head())

print("\nRows:", len(eaf_clean))
print("Columns:", len(eaf_clean.columns))

eaf_clean.to_excel(
    r"..\Output\EAF_CLEAN.xlsx",
    index=False
)

print("\nEAF_CLEAN.xlsx Created Successfully")