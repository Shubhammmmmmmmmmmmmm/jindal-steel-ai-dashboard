import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):

    st.title("🏭 Grade Wise Analysis")

    grade_table = (
        df.groupby("GRADE")
        .agg(
            Heats=("HEAT_NO","count"),
            Avg_Al=("Total_Al_kg","mean"),
            Min_Al=("Total_Al_kg","min"),
            Max_Al=("Total_Al_kg","max")
        )
        .reset_index()
    )

    st.dataframe(
        grade_table.sort_values(
            "Avg_Al",
            ascending=False
        ),
        use_container_width=True
    )

    top20 = (
        grade_table
        .sort_values(
            "Avg_Al",
            ascending=False
        )
        .head(20)
    )

    fig1 = px.bar(
        top20,
        x="GRADE",
        y="Avg_Al",
        color="Avg_Al",
        title="Top 20 Aluminium Consuming Grades"
    )

    st.plotly_chart(fig1,use_container_width=True)

    fig2 = px.pie(
        top20,
        names="GRADE",
        values="Avg_Al",
        title="Grade Contribution"
    )

    st.plotly_chart(fig2,use_container_width=True)