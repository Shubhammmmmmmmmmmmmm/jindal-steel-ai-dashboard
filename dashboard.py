import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI-Based Aluminium Optimization",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------

df = pd.read_excel(
    r"..\Output\MASTER_DATASET_FINAL_v2.xlsx"
)

model = joblib.load(
    r"..\Output\RF_Al_Model.pkl"
)

# -------------------------
# Title
# -------------------------

st.title(
    "AI-Based Aluminium Optimization System"
)

st.subheader(
    "JSPL Raigarh | SMS-LRF"
)

# -------------------------
# KPI Section
# -------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Heats",
    len(df)
)

col2.metric(
    "Average Al (kg)",
    round(df["Total_Al_kg"].mean(),1)
)

col3.metric(
    "Maximum Al (kg)",
    round(df["Total_Al_kg"].max(),1)
)

st.divider()

# -------------------------
# User Inputs
# -------------------------

st.header("Enter Heat Parameters")

col1, col2 = st.columns(2)

with col1:

    Initial_C = st.number_input(
        "Initial C",
        value=0.15
    )

    Initial_MN = st.number_input(
        "Initial Mn",
        value=1.20
    )

    Initial_SI = st.number_input(
        "Initial Si",
        value=0.15
    )

    Initial_AL = st.number_input(
        "Initial Al",
        value=0.03
    )

    Final_C = st.number_input(
        "Final C",
        value=0.18
    )

    Final_MN = st.number_input(
        "Final Mn",
        value=1.30
    )

    Final_SI = st.number_input(
        "Final Si",
        value=0.18
    )

    Final_AL = st.number_input(
        "Final Al",
        value=0.03
    )

with col2:

    Initial_N2 = st.number_input(
        "Initial N2",
        value=60.0
    )

    Final_N2 = st.number_input(
        "Final N2",
        value=65.0
    )

    Temp = st.number_input(
        "Lifting Temperature",
        value=1600.0
    )

    Process_Time = st.number_input(
        "Process Time",
        value=50.0
    )

    Power = st.number_input(
        "Power",
        value=60.0
    )

    HM = st.number_input(
        "HM %",
        value=55.0
    )

    DRI = st.number_input(
        "DRI %",
        value=35.0
    )

    Lime = st.number_input(
        "LIME",
        value=12.0
    )

    Dolo = st.number_input(
        "DOLO",
        value=1.2
    )

    CPC = st.number_input(
        "CPC",
        value=1.0
    )

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Aluminium Requirement"):

    input_df = pd.DataFrame([[
        Initial_C,
        Initial_MN,
        Initial_SI,
        Initial_AL,
        Final_C,
        Final_MN,
        Final_SI,
        Final_AL,
        Initial_N2,
        Final_N2,
        Temp,
        Process_Time,
        Power,
        HM,
        DRI,
        Lime,
        Dolo,
        CPC
    ]],
    columns=[
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
    ])

    prediction = model.predict(
        input_df
    )[0]

    st.success(
        f"Recommended Aluminium = {prediction:.1f} kg"
    )