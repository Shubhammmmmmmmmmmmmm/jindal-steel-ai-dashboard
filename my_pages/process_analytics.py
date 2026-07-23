import streamlit as st
import plotly.express as px

def app(df):

    st.title("⚙️ Process Analytics")

    grade = st.selectbox(
        "Select Grade",
        ["All"] + sorted(df["GRADE"].dropna().unique().tolist())
    )

    if grade != "All":
        df = df[df["GRADE"] == grade]

    fig1 = px.scatter(
        df,
        x="PROCESS TIME",
        y="Total_Al_kg",
        color="GRADE",
        title="Process Time vs Aluminium Consumption"
    )

    st.plotly_chart(fig1,use_container_width=True)

    fig2 = px.scatter(
        df,
        x="Final_AL",
        y="Total_Al_kg",
        title="Final Al vs Aluminium"
    )

    st.plotly_chart(fig2,use_container_width=True)

    fig3 = px.scatter(
        df,
        x="HM",
        y="Total_Al_kg",
        title="HM vs Aluminium"
    )

    st.plotly_chart(fig3,use_container_width=True)

    fig4 = px.scatter(
        df,
        x="LIFTING TEMERATURE",
        y="Total_Al_kg",
        title="Temperature vs Aluminium"
    )

    st.plotly_chart(fig4,use_container_width=True)

    fig5 = px.scatter(
        df,
        x="Final_N2",
        y="Total_Al_kg",
        title="Final N2 vs Aluminium"
    )

    st.plotly_chart(fig5,use_container_width=True)