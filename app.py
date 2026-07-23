import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
##colouring for the dashboard
st.markdown("""
<style>

[data-testid="stSidebar"]{
background:#081326;
}

[data-testid="stSidebar"] *{
color:white;
}

.main{
background-color:#f5f7fa;
}

</style>
""",
unsafe_allow_html=True)
st.set_page_config(
    page_title="Jindal Steel AI Aluminium Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

# @st.cache_data
# def load_data():
#     return pd.read_excel(
#         r"..\Code\Data\MASTER_DATASET_FINAL_v2.xlsx"
#     )

# df = load_data()
from pathlib import Path

DATA_FILE = Path("Data") / "MASTER_DATASET_FINAL_v2.xlsx"

df = pd.read_excel(DATA_FILE)

# -----------------------------
# SIDEBAR
# -----------------------------
### LOGIN PAGE###
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    if not st.session_state.logged_in:

     st.markdown("""
    <h1 style='text-align:center;color:#ff8c00;'>
    JSPL AI Aluminium Optimization System
    </h1>
    """,
    unsafe_allow_html=True)

    username = st.text_input("Employee ID")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username=="jspl" and password=="1234":

            st.session_state.logged_in=True
            st.rerun()

        else:
            st.error("Invalid Credentials")

    st.stop()


st.sidebar.title("🏭 JSPL Raigarh")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Process Analytics",
        "Grade Analysis",
        "Feature Importance",
        "Abnormal Heats",
        "AI Prediction Engine",
        "Cost Saving Analysis",
        "Recommendation Center",
        "model performance "
    ]
)

# -----------------------------
# PAGE ROUTING
# -----------------------------

if page == "Executive Overview":
    import my_pages.executive as executive
    executive.app(df)

elif page == "Process Analytics":
    import my_pages.process_analytics as process_analytics
    process_analytics.app(df)

elif page == "Grade Analysis":
    import my_pages.grade_analysis as grade_analysis
    grade_analysis.app(df)

elif page == "Feature Importance":
    import my_pages.feature_importance as feature_importance
    feature_importance.app(df)

elif page == "Abnormal Heats":
    import my_pages.abnormal_heats as abnormal_heats
    abnormal_heats.app(df)
elif page == "AI Prediction Engine":
    import my_pages.prediction_engine as prediction_engine
    prediction_engine.app(df)
elif page == "Cost Saving Analysis":

    import my_pages.cost_saving as cost_saving

    cost_saving.app(df)

elif page == "Recommendation Center":

    import my_pages.recommendations as recommendations

    recommendations.app(df)
elif page == "model performance ":

    import my_pages.model_performance as model_performance

    model_performance.app(df)
    
    