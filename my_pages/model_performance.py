import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def app(df):

    st.title("🤖 AI Model Performance")

    st.markdown("""
    Evaluation of Random Forest Model developed for Aluminium Consumption Prediction.
    """)

    # ==============================
    # KPI CARDS
    # ==============================

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "R² Score",
            "0.565"
        )

    with c2:
        st.metric(
            "MAE",
            "47.79 kg"
        )

    st.divider()

    # ==============================
    # PERFORMANCE INTERPRETATION
    # ==============================

    st.success("""
Random Forest successfully captures major aluminium consumption trends and can be used as a decision-support tool for LRF operations.

Key Points:

• R² = 0.565 indicates the model explains approximately 56.5% of variation in aluminium consumption.

• MAE = 47.79 kg means average prediction error is around 48 kg per heat.

• Suitable for process optimization and operator guidance.

• Can be further improved by adding slag chemistry, oxygen activity and real-time process data.
""")

    st.divider()

    # ==============================
    # MODEL QUALITY CHART
    # ==============================

    performance = pd.DataFrame({
        "Metric":["R² Score","Model Accuracy"],
        "Value":[0.565,56.5]
    })

    fig = px.bar(
        performance,
        x="Metric",
        y="Value",
        color="Value",
        title="Random Forest Model Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Actual vs Predicted Concept")

    st.info("""
In the original model development stage, Actual vs Predicted Aluminium Consumption scatter plots were generated.

An ideal model would place all points on the 45° line.

The Random Forest model shows good agreement with actual plant data and captures the dominant process trends affecting aluminium consumption.
""")