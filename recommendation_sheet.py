import pandas as pd

master = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

print(master.shape)
grade_summary = (
    master.groupby("GRADE")["Total_Al_kg"]
    .agg(
        Heats="count",
        Avg_Al="mean",
        Min_Al="min",
        Max_Al="max"
    )
    .sort_values(
        by="Avg_Al",
        ascending=False
    )
)

print(grade_summary.head(20))

grade_summary.to_excel(
    r"..\Output\Grade_Aluminium_Benchmark.xlsx"
)


####RECOMENDATION 2

top_heats = master[
    [
        "HEAT_NO",
        "GRADE",
        "Total_Al_kg",
        "Final_AL",
        "PROCESS TIME",
        "LIFTING TEMERATURE"
    ]
].sort_values(
    by="Total_Al_kg",
    ascending=False
)

print(top_heats.head(20))

top_heats.to_excel(
    r"..\Output\Top_20_Aluminium_Heats.xlsx",
    index=False
)

#####RECOMMENDATION 3
avg_al = master["Total_Al_kg"].mean()

saving_percent = 5

saving_per_heat = avg_al * saving_percent / 100

print("Average Al =", avg_al)

print("Saving Per Heat =", saving_per_heat)


########## Recommendation 4: Create Final Project Flow Diagram

# This will go into PPT.

# EAF Heat
#       ↓
# LRF Input Chemistry
#       ↓
# Temperature
#       ↓
# Nitrogen
#       ↓
# Process Time
#       ↓
# Random Forest Model
#       ↓
# Predicted Al Requirement
#       ↓
# Recommended Al Addition
#       ↓
# Cost Saving

####Recommendation 5: Create Final Correlation Table

corr = master.select_dtypes(
    include="number"
).corr()

corr["Total_Al_kg"]\
.sort_values(
    ascending=False
)\
.to_excel(
    r"..\Output\Correlation_With_Al.xlsx"
)
