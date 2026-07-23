# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# # print(
#     df.groupby("Batch Number")
#       ["Inspection Pt"]
#       .count()
#       .sort_values(ascending=False)
#       .head(20)
# )
# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# print("Rows =", len(df))

# print("Unique Heats =",
#       df["Batch Number"].nunique())
# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# print("Rows =", len(df))

# print("Unique Heats =",
#       df["Batch Number"].nunique())
# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# heat = 4615002

# print(
#     df[df["Batch Number"] == heat]
#     [["Batch Number",
#       "Inspection Pt",
#       "Machine Info",
#       "C",
#       "MN",
#       "SI",
#       "AL"]]
# )
# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# f_samples = df[
#     df["Inspection Pt"].astype(str).str.startswith("F")
# ]

# print("Unique heats with F samples =",
#       f_samples["Batch Number"].nunique())

# print("Total unique heats =",
#       df["Batch Number"].nunique())


# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# # Keep only F and L samples
# df = df[
#     df["Inspection Pt"].astype(str)
#       .str.match(r'^[FL]\d+$', na=False)
# ].copy()

# # Extract sample number
# df["sample_no"] = (
#     df["Inspection Pt"]
#       .str.extract(r'(\d+)')
#       .astype(int)
# )

# print(df.head())

# print("\nRows:", len(df))
# import pandas as pd

# df = pd.read_excel(r"..\Output\COMPO_ALL.xlsx")

# # Keep only F and L samples
# df = df[
#     df["Inspection Pt"].astype(str)
#       .str.match(r'^[FL]\d+$', na=False)
# ].copy()

# # Sample type
# df["sample_type"] = (
#     df["Inspection Pt"]
#       .str[0]
# )

# Sample number
# df["sample_no"] = (
#     df["Inspection Pt"]
#       .str.extract(r'(\d+)')
#       .astype(int)
# )

# Highest F sample per heat
# initial = (
#     df[df["sample_type"]=="F"]
#     .sort_values("sample_no")
#     .groupby("Batch Number")
#     .tail(1)
# )

# Highest L sample per heat
# final = (
#     df[df["sample_type"]=="L"]
#     .sort_values("sample_no")
#     .groupby("Batch Number")
#     .tail(1)
# )
# # Highest L sample per heat
# final = (
#     df[df["sample_type"]=="L"]
#     .loc[
#         df[df["sample_type"]=="L"]
#         .groupby("Batch Number")["sample_no"]
#         .idxmax()
#     ]
# )

# print(
#     final["Inspection Pt"]
#     .value_counts()
#     .sort_index()
# )

# print("Initial heats =", len(initial))
# print("Final heats   =", len(final))

# print("\nInitial Sample Example")
# print(
#     initial[
#         ["Batch Number",
#          "Inspection Pt",
#          "C",
#          "MN",
#          "SI",
#          "AL"]
#     ].head()
# )

# print("\nFinal Sample Example")
# print(
#     final[
#         ["Batch Number",
#          "Inspection Pt",
#          "C",
#          "MN",
#          "SI",
#          "AL"]
#     ].head()
# )
# # heat = 4615002

# print(
#     df[df["Batch Number"] == heat]
#     [["Batch Number","Inspection Pt","sample_no"]]
#     .sort_values("sample_no")
# )

# Rename Initial Chemistry Columns

# initial = initial.rename(columns={
#     "C": "Initial_C",
#     "MN": "Initial_MN",
#     "SI": "Initial_SI",
#     "S": "Initial_S",
#     "AL": "Initial_AL",
#     "N2": "Initial_N2",
#     "O2": "Initial_O2"
# })

# # Rename Final Chemistry Columns

# final = final.rename(columns={
#     "C": "Final_C",
#     "MN": "Final_MN",
#     "SI": "Final_SI",
#     "S": "Final_S",
#     "AL": "Final_AL",
#     "N2": "Final_N2",
#     "O2": "Final_O2"
# })

# # Keep Required Columns

# initial = initial[
#     [
#         "Batch Number",
#         "Initial_C",
#         "Initial_MN",
#         "Initial_SI",
#         "Initial_S",
#         "Initial_AL",
#         "Initial_N2",
#         "Initial_O2"
#     ]
# ]

# final = final[
#     [
#         "Batch Number",
#         "Final_C",
#         "Final_MN",
#         "Final_SI",
#         "Final_S",
#         "Final_AL",
#         "Final_N2",
#         "Final_O2"
#     ]
# ]

# # Merge

# chem_master = pd.merge(
#     initial,
#     final,
#     on="Batch Number",
#     how="outer"
# )

# print("\nChemistry Master Shape:")
# print(chem_master.shape)

# chem_master.to_excel(
#     r"..\Output\CHEMISTRY_MASTER.xlsx",
#     index=False
# )

# print("\nCHEMISTRY_MASTER.xlsx Created Successfully")
# import pandas as pd

# lrf = pd.read_excel(r"..\Output\LRF_CLEAN.xlsx")
# eaf = pd.read_excel(r"..\Output\EAF_CLEAN.xlsx")
# chem = pd.read_excel(r"..\Output\CHEMISTRY_MASTER.xlsx")

# print("\nLRF Columns:")
# print(lrf.columns.tolist())

# print("\nEAF Columns:")
# print(eaf.columns.tolist())

# print("\nCHEM Columns:")
# print(chem.columns.tolist())
# import pandas as pd

# # Load files

# lrf = pd.read_excel(r"..\Output\LRF_CLEAN.xlsx")
# eaf = pd.read_excel(r"..\Output\EAF_CLEAN.xlsx")
# chem = pd.read_excel(r"..\Output\CHEMISTRY_MASTER.xlsx")

# # # Standardize heat number names

# lrf = lrf.rename(columns={
#     "HEAT NO": "HEAT_NO"
# })

# eaf = eaf.rename(columns={
#     "H NO.": "HEAT_NO"
# })

# chem = chem.rename(columns={
#     "Batch Number": "HEAT_NO"
# })

# # # Convert to numeric

# lrf["HEAT_NO"] = pd.to_numeric(lrf["HEAT_NO"], errors="coerce")
# eaf["HEAT_NO"] = pd.to_numeric(eaf["HEAT_NO"], errors="coerce")
# chem["HEAT_NO"] = pd.to_numeric(chem["HEAT_NO"], errors="coerce")

# # Merge LRF + Chemistry

# master = pd.merge(
#     lrf,
#     chem,
#     on="HEAT_NO",
#     how="left"
# )

# print("After LRF + Chemistry:")
# print(master.shape)

# # Merge EAF

# master = pd.merge(
#     master,
#     eaf,
#     on="HEAT_NO",
#     how="left"
# )

# print("Final Master Shape:")
# print(master.shape)

# # Save

# master.to_excel(
#     r"..\Output\MASTER_DATASET_FINAL.xlsx",
#     index=False
# )


# print("\nMASTER_DATASET_FINAL.xlsx Created Successfully")
# print(
#     eaf["HEAT_NO"]
#     .value_counts()
#     .head(20)
# )
# print("LRF rows :", len(lrf))
# print("LRF unique heats :", lrf["HEAT_NO"].nunique())

# print("EAF rows :", len(eaf))
# print("EAF unique heats :", eaf["HEAT_NO"].nunique())

# dup_lrf = lrf["HEAT_NO"].value_counts()

# print(
#     dup_lrf[dup_lrf > 1]
#     .head(20)
# )
# dup_chem = chem["HEAT_NO"].value_counts()

# print(
#     dup_chem[dup_chem > 1]
#     .head(20)
# )
# print(lrf["HEAT_NO"].dtype)
# print(eaf["HEAT_NO"].dtype)
# print(chem["HEAT_NO"].dtype)

# print(
#     lrf[
#         lrf["HEAT_NO"] == 4615761
#     ]
# )
# print(
#     lrf[
#         lrf["HEAT_NO"] == 4615761
#     ][
#         [
#             "HEAT_NO",
#             "Date",
#             "GRADE",
#             "LIFTING TEMERATURE",
#             "PROCESS TIME",
#             "total al (kg)"
#         ]
#     ]
# )
# dup_heats = lrf["HEAT_NO"].value_counts()

# print(
#     dup_heats[dup_heats > 1]
# )
# for heat in [4616541, 4617290, 4617518, 4617519]:
#     print("\nHEAT =", heat)
#     print(
#         lrf[lrf["HEAT_NO"] == heat][
#             ["HEAT_NO","GRADE","LIFTING TEMERATURE","PROCESS TIME"]
#         ]
#     )

# lrf = lrf.drop_duplicates()
# print("Before:", len(lrf))

# lrf = lrf.drop_duplicates()

# print("After :", len(lrf))
# lrf = lrf[lrf["HEAT_NO"] != 4615761]

# import pandas as pd

# master = pd.read_excel(
#     r"..\Output\MASTER_DATASET_FINAL.xlsx"
# )

# print(master[
#     [
#         "total al (kg)",
#         "Initial_AL",
#         "Final_AL",
#         "FeO (in slag)",
#         "Basicity B1",
#         "LIFTING TEMERATURE"
#     ]
# ].info())

# lrf = pd.read_excel(r"..\Output\LRF_CLEAN.xlsx")

# print(
#     lrf[
#         [
#             "total al (kg)",
#             "FeO (in slag)",
#             "Basicity B1"
#         ]
#     ].info()
# )
# print(
#     lrf[
#         [
#             "total al (kg)",
#             "FeO (in slag)",
#             "Basicity B1"
#         ]
#     ].head(20)
# )

# import pandas as pd

# raw = pd.read_excel(
#     r"..\Data\lrf_sheet.xlsx"
# )

# print(raw[
#     [
#         "total al (kg)",
#         "FeO (in slag)",
#         "Basicity B1"
#     ]
# ].head(20))
import pandas as pd

# raw = pd.read_excel(r"..\Data\lrf_sheet.xlsx")

# print(raw.columns.tolist())
# lrf = pd.read_excel(
#     r"..\Output\LRF_CLEAN_UPDATED.xlsx"
# )
# print(lrf.columns.tolist())
lrf = pd.read_excel(r"..\Output\LRF_CLEAN_UPDATED.xlsx")
eaf = pd.read_excel(r"..\Output\EAF_CLEAN.xlsx")
chem = pd.read_excel(r"..\Output\CHEMISTRY_MASTER.xlsx")
