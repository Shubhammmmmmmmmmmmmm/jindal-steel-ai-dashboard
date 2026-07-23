# import pandas as pd
# lrf = pd.read_excel( r"..\Data\lrf_sheet.xlsx", header=0)
# print(lrf.head())
# print("\nRows:", len(lrf))
# print("\nColumns:", len(lrf.columns))
# for col in lrf.columns:
#     print(repr(col))
# keep_cols = [
#     'Date',
#     'HEAT NO',
#     'GRADE',
#     'VD/NVD',

#     'LIFTING TEMERATURE',
#     'POWER',
#     'PROCESS TIME',
#     'TEMP OPENING',
#     'argon flow rate',

#     'AL SHOTS',
#     'al ingot',
#     'al wire (mtr)',
#     'total al (kg)',
#     'Al (kg/ton)',

#     'Initial C',
#     'Initial S',
#     'initial mn',
#     'initial si',
#     'initial Al',
#     'O₂ ppm',

#     'final %C',
#     'final %S',
#     'final  %AL',
#     'final %MN',
#     'final %Si',

#     'Sulphur Removal %',

#     'FeO (in slag)',
#     'CaO(in slag)',
#     'SiO₂(in slag)',
#     'Al₂O₃',
#     'MnO',

#     'Basicity B1',
#     'Basicity B2',

#     'SIMN',
#     'FeMn(add)',
#     'FESI',
#     'casi wire(mtr)',

#     'LIME',
#     'SPAR'
# ]
# lrf_clean = lrf[keep_cols]
# print(lrf_clean.head())
# print("\nRows:", len(lrf_clean))
# print("Columns:", len(lrf_clean.columns))
# lrf_clean.to_excel(r"..\Output\LRF_CLEAN.xlsx", index=False)
# print("\nLRF_CLEAN.xlsx Created Successfully")

# import pandas as pd

# raw = pd.read_excel(r"..\Data\lrf_sheet.xlsx")

# print(
#     raw[
#         [
#             "total al (kg)",
#             "FeO (in slag)",
#             "Basicity B1"
#         ]
#     ].info()
# )

# print(
#     raw[
#         [
#             "total al (kg)",
#             "FeO (in slag)",
#             "Basicity B1"
#         ]
#     ].head(20)
# )

# import pandas as pd

# lrf = pd.read_excel(r"..\Data\lrf_sheet.xlsx")

# print(
#     lrf[
#         [
#             "AL SHOTS",
#             "al ingot",
#             "al wire (mtr)",
#             "total al (kg)"
#         ]
#     ].info()
# )

# print(
#     lrf[
#         [
#             "AL SHOTS",
#             "al ingot",
#             "al wire (mtr)",
#             "total al (kg)"
#         ]
#     ].head(20)
# )

import pandas as pd

lrf = pd.read_excel(r"..\Output\LRF_CLEAN.xlsx")

# # Fill blank values with 0
# lrf["AL SHOTS"] = lrf["AL SHOTS"].fillna(0)
# lrf["al ingot"] = lrf["al ingot"].fillna(0)
# lrf["al wire (mtr)"] = lrf["al wire (mtr)"].fillna(0)

# # Convert wire length to kg
# lrf["Al_wire_kg"] = lrf["al wire (mtr)"] * 0.33

# # Calculate total aluminium
# lrf["Total_Al_kg"] = (
#     lrf["AL SHOTS"] +
#     lrf["al ingot"] +
#     lrf["Al_wire_kg"]
# )

# # Aluminium consumption per ton
# lrf["Al_kg_per_ton"] = (
#     lrf["Total_Al_kg"] /
#     lrf["STEEL WEIGHT(in ton)(TAPPING)"]
# )

# print(
#     lrf[
#         [
#             "AL SHOTS",
#             "al ingot",
#             "al wire (mtr)",
#             "Al_wire_kg",
#             "Total_Al_kg",
#             "Al_kg_per_ton"
#         ]
#     ].head()
# )

# lrf.to_excel(
#     r"..\Output\LRF_CLEAN_UPDATED.xlsx",
#     index=False
# )

# print("LRF_CLEAN_UPDATED.xlsx Created Successfully")

# for col in lrf.columns:
#     print(repr(col))

lrf["AL SHOTS"] = lrf["AL SHOTS"].fillna(0)
lrf["al ingot"] = lrf["al ingot"].fillna(0)
lrf["al wire (mtr)"] = lrf["al wire (mtr)"].fillna(0)

lrf["Al_wire_kg"] = lrf["al wire (mtr)"] * 0.33

lrf["Total_Al_kg"] = (
    lrf["AL SHOTS"]
    + lrf["al ingot"]
    + lrf["Al_wire_kg"]
)

print(
    lrf[
        [
            "AL SHOTS",
            "al ingot",
            "al wire (mtr)",
            "Al_wire_kg",
            "Total_Al_kg"
        ]
    ].head()
)
print(lrf["Total_Al_kg"].describe())

lrf.to_excel(
    r"..\Output\LRF_CLEAN_UPDATED.xlsx",
    index=False
)

print("LRF_CLEAN_UPDATED.xlsx Created Successfully")