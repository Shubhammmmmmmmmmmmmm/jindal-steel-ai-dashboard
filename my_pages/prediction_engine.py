import streamlit as st
import pandas as pd
import joblib


def app(df):

    st.title("🤖 AI Aluminium Recommendation Engine")

    st.markdown("""
    Enter steel chemistry and process parameters to predict
    Aluminium Requirement using the trained Random Forest Model.
    """)

    # ==================================
    # Load Model
    # ==================================

    model = joblib.load(
        r"../Code/Output/RF_Al_Model.pkl"
    )

    st.subheader("Input Parameters")

    col1, col2 = st.columns(2)

    with col1:

        Initial_C = st.number_input("Initial_C", value=0.20)
        Initial_MN = st.number_input("Initial_MN", value=0.80)
        Initial_SI = st.number_input("Initial_SI", value=0.05)
        Initial_AL = st.number_input("Initial_AL", value=0.30)

        Final_C = st.number_input("Final_C", value=0.18)
        Final_MN = st.number_input("Final_MN", value=1.20)
        Final_SI = st.number_input("Final_SI", value=0.20)
        Final_AL = st.number_input("Final_AL", value=0.03)

        Initial_N2 = st.number_input("Initial_N2", value=55.0)

    with col2:

        Final_N2 = st.number_input("Final_N2", value=65.0)

        LIFTING_TEMPERATURE = st.number_input(
            "LIFTING TEMERATURE",
            value=1590.0
        )

        PROCESS_TIME = st.number_input(
            "PROCESS TIME",
            value=50.0
        )

        POWER_y = st.number_input(
            "POWER_y",
            value=30000.0
        )

        HM = st.number_input(
            "HM",
            value=60.0
        )

        DRI = st.number_input(
            "DRI",
            value=40.0
        )

        LIME_y = st.number_input(
            "LIME_y",
            value=12.0
        )

        DOLO = st.number_input(
            "DOLO",
            value=1.2
        )

        CPC = st.number_input(
            "CPC",
            value=380.0
        )

    if st.button("Predict Aluminium Requirement"):

        input_df = pd.DataFrame([{

            "Initial_C": Initial_C,
            "Initial_MN": Initial_MN,
            "Initial_SI": Initial_SI,
            "Initial_AL": Initial_AL,

            "Final_C": Final_C,
            "Final_MN": Final_MN,
            "Final_SI": Final_SI,
            "Final_AL": Final_AL,

            "Initial_N2": Initial_N2,
            "Final_N2": Final_N2,

            "LIFTING TEMERATURE": LIFTING_TEMPERATURE,
            "PROCESS TIME": PROCESS_TIME,

            "POWER_y": POWER_y,
            "HM": HM,
            "DRI": DRI,
            "LIME_y": LIME_y,
            "DOLO": DOLO,
            "CPC": CPC

        }])

        prediction = model.predict(input_df)[0]

        st.success(
            f"Predicted Aluminium Requirement = {prediction:.2f} kg"
        )

        if prediction < 200:

            st.success("🟢 Low Aluminium Requirement")

        elif prediction < 300:

            st.warning("🟡 Moderate Aluminium Requirement")

        else:

            st.error("🔴 High Aluminium Requirement")

        st.metric(
            "Predicted Al (kg)",
            round(prediction, 2)
        )