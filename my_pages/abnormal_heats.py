import streamlit as st
import plotly.express as px

def app(df):

    st.title("🚨 Abnormal Heat Detection")

    abnormal = df[
        df["Total_Al_kg"] > 500
    ]

    st.metric(
        "Abnormal Heats",
        len(abnormal)
    )

    st.dataframe(
        abnormal[
            [
                "HEAT_NO",
                "GRADE",
                "Total_Al_kg",
                "PROCESS TIME",
                "Final_AL"
            ]
        ],
        use_container_width=True
    )

    fig = px.box(
        df,
        y="Total_Al_kg",
        title="Outlier Detection"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig2 = px.bar(
        abnormal.sort_values(
            "Total_Al_kg",
            ascending=False
        ).head(20),
        x="HEAT_NO",
        y="Total_Al_kg",
        color="Total_Al_kg",
        title="Top Aluminium Consuming Heats"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )