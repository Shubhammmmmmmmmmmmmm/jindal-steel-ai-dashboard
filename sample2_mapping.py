import pandas as pd

lrf = pd.read_excel(r"..\Output\LRF_CLEAN_UPDATED.xlsx")
eaf = pd.read_excel(r"..\Output\EAF_CLEAN.xlsx")
chem = pd.read_excel(r"..\Output\CHEMISTRY_MASTER.xlsx")
lrf = lrf.rename(columns={"HEAT NO": "HEAT_NO"})
eaf = eaf.rename(columns={"H NO.": "HEAT_NO"})
eaf = eaf[
    [
        "HEAT_NO",
        "HM",
        "DRI",
        "LIME",
        "DOLO",
        "CPC",
        "POWER",
        "OXY",
        "Production"
    ]
]
master = pd.merge(
    lrf,
    chem,
    left_on="HEAT_NO",
    right_on="Batch Number",
    how="left"
)

print("After LRF + Chemistry:")
print(master.shape)

master = pd.merge(
    master,
    eaf,
    on="HEAT_NO",
    how="left"
)

print("Final Master Shape:")
print(master.shape)
# master["Al_kg_per_ton"] = (
#     master["Total_Al_kg"] /
#     master["Production"]
# )
print(master.shape)

important_cols = [
    "Total_Al_kg",
    "Initial_AL",
    "Final_AL",
    "Initial_O2",
    "Final_O2",
    "LIFTING TEMERATURE"
]

# print(master[important_cols].info())
# master["LIFTING TEMERATURE"] = pd.to_numeric(
#     master["LIFTING TEMERATURE"],
#     errors="coerce"
# )

# print(master["LIFTING TEMERATURE"].dtype)
# master["Al_kg_per_ton"] = (
#     master["Total_Al_kg"] / 100
# )
# drop_cols = [
#     "Initial C",
#     "Initial S",
#     "initial mn",
#     "initial si",
#     "initial Al",
#     "O₂ ppm",
#     "final %C",
#     "final %S",
#     "final  %AL",
#     "final %MN",
#     "final %Si"
# ]

# master = master.drop(
#     columns=drop_cols,
#     errors="ignore"
# )

# print(master.shape)
# master.to_excel(
#     r"..\Output\MASTER_DATASET_FINAL_v2.xlsx",
#     index=False
# )

# print("MASTER_DATASET_FINAL_v2.xlsx Created Successfully")
# print(master.shape)

# important_cols = [
#     "HEAT_NO",
#     "Total_Al_kg",
#     "Al_kg_per_ton",
#     "Initial_AL",
#     "Final_AL",
#     "Initial_O2",
#     "Final_O2",
#     "LIFTING TEMERATURE",
#     "PROCESS TIME"
# ]

# print(master[important_cols].info())
master["LIFTING TEMERATURE"] = pd.to_numeric(
    master["LIFTING TEMERATURE"],
    errors="coerce"
)

print(master["LIFTING TEMERATURE"].dtype)
drop_cols = [
    "Initial C",
    "Initial S",
    "initial mn",
    "initial si",
    "initial Al",
    "O₂ ppm",
    "final %C",
    "final %S",
    "final  %AL",
    "final %MN",
    "final %Si"
]

master = master.drop(
    columns=drop_cols,
    errors="ignore"
)

# print(master.shape)
# print(
#     master["Al (kg/ton)"]
#     .describe()
# )

# print(master[
# [
#     "Total_Al_kg",
#     "Initial_AL",
#     "Final_AL",
#     "Initial_O2",
#     "Final_O2",
#     "LIFTING TEMERATURE",
#     "PROCESS TIME"
# ]
# ].describe())

# print(master["Initial_O2"].value_counts().head(10))
# print(master["Final_O2"].value_counts().head(10))

master = master.drop(
    columns=[
        "Initial_O2",
        "Final_O2"
    ],
    errors="ignore"
 )
# print(
#     master[
#         master["LIFTING TEMERATURE"] < 1400
#     ][["HEAT_NO","LIFTING TEMERATURE"]]
# )
# print(
#     master[
#         master["HEAT_NO"] == 4615592
#     ].T
# )
# master = master[
#     master["LIFTING TEMERATURE"] >= 1400
# ]

# # print(master.shape)

# print(
#     master["LIFTING TEMERATURE"]
#     .isna()
#     .sum()
# )


# important_cols = [
#     "HEAT_NO",
#     "Total_Al_kg",
#     "Initial_AL",
#     "Final_AL",
#     "Initial_O2",
#     "Final_O2",
#     "LIFTING TEMERATURE",
#     "PROCESS TIME"
# ]

# print(master[important_cols].describe())
master.to_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx",
    index=False
)