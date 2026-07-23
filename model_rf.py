# import pandas as pd

# df = pd.read_excel(
#     r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
# )

# # print(df.shape)
# # print(df.columns.tolist())

# # print(
# #     df.isna().sum()
# #     .sort_values(ascending=False)
# #     .head(20)
# # )

# # print(
# #     df["Total_Al_kg"]
# #     .describe()
# # )


# # features = [
# #     "Initial_C",
# #     "Initial_MN",
# #     "Initial_SI",
# #     "Initial_AL",

# #     "Final_C",
# #     "Final_MN",
# #     "Final_SI",
# #     "Final_AL",

# #     "Initial_N2",
# #     "Final_N2",

# #     "LIFTING TEMERATURE",
# #     "PROCESS TIME",

# #     "POWER_y",
# #     "HM",
# #     "DRI",
# #     "LIME_y",
# #     "DOLO"
# # ]

# # target = "Total_Al_kg"

# # for col in features:
# #     if col not in df.columns:
# #         print("Missing:", col)

# features = [
#     "Initial_C",
#     "Initial_MN",
#     "Initial_SI",
#     "Initial_AL",

#     "Final_C",
#     "Final_MN",
#     "Final_SI",
#     "Final_AL",

#     "Initial_N2",
#     "Final_N2",

#     "LIFTING TEMERATURE",
#     "PROCESS TIME",

#     "POWER_y",
#     "HM",
#     "DRI",
#     "LIME_y",
#     "DOLO",
#     "CPC"
# ]

# target = "Total_Al_kg"

# model_df = df[features + [target]].copy()

# print(model_df.shape)
# print(model_df.isna().sum())
# model_df = model_df.dropna()

# print("\nAfter Cleaning")
# print(model_df.shape)

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import r2_score, mean_absolute_error

# # -------------------------
# # Load data
# # -------------------------

# df = pd.read_excel(
#     # r"..\Code\Data\Output\MASTER_DATASET_FINAL_v2.xlsx"
# )

# features = [
#     "Initial_C",
#     "Initial_MN",
#     "Initial_SI",
#     "Initial_AL",

#     "Final_C",
#     "Final_MN",
#     "Final_SI",
#     "Final_AL",

#     "Initial_N2",
#     "Final_N2",

#     "LIFTING TEMERATURE",
#     "PROCESS TIME",

#     "POWER_y",
#     "HM",
#     "DRI",
#     "LIME_y",
#     "DOLO",
#     "CPC"
# ]
# for col in features:
#     # print("\n", col)
#     # print(df[col].dtype)

#     if df[col].dtype == "object":
#         print(
#             df[col]
#             .value_counts()
#             .head(20)
#         )
# for col in features:
#     df[col] = pd.to_numeric(
#         df[col],
#         errors="coerce"
#     )
    
    
# target = "Total_Al_kg"

# model_df = df[features + [target]].copy()

# model_df = model_df.dropna()
# # print(
# #          model_df[features]
# #     .dtypes
# # )
# # print("Final Model Data Shape:")
# # print(model_df.shape)

# # -------------------------
# # X and y
# # -------------------------

# X = model_df[features]

# y = model_df[target]

# # -------------------------
# # Train Test Split
# # -------------------------

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42
# )

# # print("Train Size:", len(X_train))
# # print("Test Size :", len(X_test))

# # -------------------------
# # Random Forest
# # -------------------------

# rf = RandomForestRegressor(
#     n_estimators=300,
#     random_state=42,
#     n_jobs=-1
# )

# rf.fit(X_train, y_train)

# # -------------------------
# # Prediction
# # -------------------------

# y_pred = rf.predict(X_test)
# import matplotlib.pyplot as plt

# plt.figure(figsize=(8,6))

# plt.scatter(
#     y_test,
#     y_pred,
#     alpha=0.6
# )

# plt.plot(
#     [y_test.min(), y_test.max()],
#     [y_test.min(), y_test.max()],
#     'r--'
# )

# plt.xlabel("Actual Al (kg)")
# plt.ylabel("Predicted Al (kg)")
# plt.title("Actual vs Predicted Aluminium Consumption")

# plt.grid(True)

# plt.show()

# # -------------------------
# # Accuracy
# # -------------------------

# r2 = r2_score(y_test, y_pred)

# mae = mean_absolute_error(
#     y_test,
#     y_pred
# )

# print("\nR2 Score =", round(r2,4))
# print("MAE =", round(mae,2),"kg")

# import pandas as pd
# import matplotlib.pyplot as plt

# importance = pd.DataFrame({
#     "Feature": features,
#     "Importance": rf.feature_importances_
# })

# importance = (
#     importance
#     .sort_values(
#         by="Importance",
#         ascending=False
#     )
# )

# print("\nFeature Importance")
# print(importance)

# plt.figure(figsize=(10,6))

# plt.barh(
#     importance["Feature"],
#     importance["Importance"]
# )

# plt.xlabel("Importance")
# plt.title(
#     "Random Forest Feature Importance"
# )

# plt.gca().invert_yaxis()

# plt.show()



# plt.figure(figsize=(8,6))

# plt.scatter(
#     y_test,
#     y_pred,
#     alpha=0.6
# )

# plt.xlabel("Actual Al (kg)")
# plt.ylabel("Predicted Al (kg)")
# plt.title(
#     "Actual vs Predicted Aluminium Consumption"
# )

# plt.grid(True)

# plt.show()
# import joblib

# joblib.dump(
#     rf,
#     r"..\Code\Data\Output\RF_Al_Model.pkl"
# )

# print("Model Saved Successfully")
# feature_importance = pd.DataFrame({
#     "Feature": X.columns,
#     "Importance": rf.feature_importances_
# })

# feature_importance = feature_importance.sort_values(
#     by="Importance",
#     ascending=False
# )

# print(feature_importance)

# feature_importance.to_excel(
#     r"..\Code\Data\Output\RF_Feature_Importance.xlsx",
#     index=False
# )

# print("Feature Importance Saved")



########corect version of code of model_rf.py

import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_excel(
    r"Data\MASTER_DATASET_FINAL_v2.xlsx"
)

print("Dataset Shape:")
print(df.shape)


# ==========================================
# FEATURES
# ==========================================

features = [

    "Initial_C",
    "Initial_MN",
    "Initial_SI",
    "Initial_AL",

    "Final_C",
    "Final_MN",
    "Final_SI",
    "Final_AL",

    "Initial_N2",
    "Final_N2",

    "LIFTING TEMERATURE",
    "PROCESS TIME",

    "POWER_y",
    "HM",
    "DRI",
    "LIME_y",
    "DOLO",
    "CPC"

]

target = "Total_Al_kg"


# ==========================================
# CONVERT OBJECT TO NUMERIC
# ==========================================

for col in features:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


# ==========================================
# MODEL DATA
# ==========================================

model_df = df[features + [target]].copy()

model_df = model_df.dropna()

print("\nFinal Model Data Shape:")
print(model_df.shape)


# ==========================================
# X AND Y
# ==========================================

X = model_df[features]

y = model_df[target]


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42

)

print("\nTrain Size:", len(X_train))
print("Test Size :", len(X_test))


# ==========================================
# RANDOM FOREST
# ==========================================

rf = RandomForestRegressor(

    n_estimators=300,

    random_state=42,

    n_jobs=-1

)

rf.fit(X_train, y_train)


# ==========================================
# PREDICTIONS
# ==========================================


y_pred = rf.predict(X_test)
  
  # ==========================================
# SAVE ACTUAL VS PREDICTED
# ==========================================

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

results.to_excel(
    r"Output\RF_Predictions.xlsx",
    index=False
)

print("RF_Predictions.xlsx Saved")
# Save Actual vs Predicted values

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

results.to_excel(
    r"Output\RF_Predictions.xlsx",
    index=False
)

print("RF_Predictions.xlsx Saved")

# ==========================================
# MODEL PERFORMANCE
# ==========================================

r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(
    y_test,
    y_pred
)

print("\nR2 Score =", round(r2, 4))
print("MAE =", round(mae, 2), "kg")


# ==========================================
# FEATURE IMPORTANCE
# ==========================================

feature_importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": rf.feature_importances_

})

feature_importance = feature_importance.sort_values(

    by="Importance",

    ascending=False

)

print("\nFeature Importance")

print(feature_importance)


# ==========================================
# SAVE FEATURE IMPORTANCE
# ==========================================

feature_importance.to_excel(

    r"Output\RF_Feature_Importance.xlsx",

    index=False

)

print("\nFeature Importance Saved")


# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(

    rf,

    r"Output\RF_Al_Model.pkl"

)

print("Model Saved Successfully")


# ==========================================
# GRAPH 1
# Actual vs Predicted
# ==========================================

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

plt.plot(

    [y_test.min(), y_test.max()],

    [y_test.min(), y_test.max()],

    "r--"

)

plt.xlabel("Actual Al (kg)")
plt.ylabel("Predicted Al (kg)")
plt.title("Actual vs Predicted Aluminium")

plt.grid(True)

plt.show()


# ==========================================
# GRAPH 2
# Feature Importance
# ==========================================

plt.figure(figsize=(10,6))

plt.barh(

    feature_importance["Feature"],

    feature_importance["Importance"]

)

plt.xlabel("Importance")

plt.title(

    "Random Forest Feature Importance"

)

plt.gca().invert_yaxis()

plt.grid(True)

plt.show()


