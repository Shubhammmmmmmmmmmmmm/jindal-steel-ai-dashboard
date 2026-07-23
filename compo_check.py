# # import pandas as pd

# # compo = pd.read_excel(
# #     r"..\Data\compo_data_apr-june.xlsx"
# # )

# # print("Rows:", len(compo))

# # print("\nColumns:\n")

# # for col in compo.columns:
# #     print(repr(col))

# # import pandas as pd
# # df = pd.read_excel( r"..\Data\Lab Data - Jan - May - 2026 (1).xlsx",  sheet_name="APRIL - 26", header=None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', 30)
# # # print(df.head(20))
# # # print(df[['Batch Number',
# # #           'Machine Info',
# # #           'Inspection Pt']].head(30))

# # for i, col in enumerate(df.columns):
# #     print(i, repr(col))

# # import pandas as pd

# # # df = pd.read_excel(
# # #     r"..\Data\Lab Data - Jan - May - 2026 (1).xlsx",
# # #     sheet_name="APRIL - 26",
# # #     header=None
# # # )

# # # for i in range(15):
# # #     print(f"\nROW {i}")
# # #     print(df.iloc[i].tolist())
# # df = pd.read_excel(
# #     r"..\Data\Lab Data - Jan - May - 2026 (1).xlsx",
# #     sheet_name="APRIL - 26",
# #     header=6
# # )
# # df.columns = df.columns.str.strip()
# # print(df.columns.tolist())
# import pandas as pd

# df = pd.read_excel(
#     r"..\Data\Lab Data - Jan - May - 2026 (1).xlsx",sheet_name="JUNE - 26", header=6)

# df.columns = df.columns.str.strip()

# keep_cols = [
#     'Status',
#     'Date',
#     'Machine Info',
#     'Inspection Pt',
#     'Batch Number',
#     'C',
#     'MN',
#     'SI',
#     'S',
#     'P',
#     'AL',
#     'CR',
#     'NB',
#     'V',
#     'TI',
#     'N2',
#     'O2'
# ]

# compo_june = df[keep_cols]

# # Remove blank rows
# compo_june = compo_june.dropna(subset=['Batch Number'])

# print(compo_june.head())

# compo_june.to_excel(
#     r"..\Output\COMPO_JUNE.xlsx",
#     index=False
# )

# print("COMPO_JUNE.xlsx Created Successfully")
# import pandas as pd

# april = pd.read_excel(r"..\Output\COMPO_APRIL.xlsx")
# may   = pd.read_excel(r"..\Output\COMPO_MAY.xlsx")
# june  = pd.read_excel(r"..\Output\COMPO_JUNE.xlsx")

# compo_all = pd.concat(
#     [april, may, june],
#     ignore_index=True
# )

# print(compo_all.shape)

# compo_all.to_excel(
#     r"..\Output\COMPO_ALL.xlsx",
#     index=False
# )

# print("COMPO_ALL Created Successfully")

import pandas as pd

df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

print(df["Inspection Pt"].value_counts())