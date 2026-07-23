import streamlit as st
st.markdown("""
<div style="
background:linear-gradient(90deg,#081326,#162544);
padding:30px;
border-radius:15px;
">

<h1 style="
color:white;
">
AI-Based Aluminium Optimization System
</h1>

<h3 style="
color:#ff8c00;
">
JSPL Raigarh | SMS-LRF
</h3>

</div>
""",
unsafe_allow_html=True)

def app(df):

    st.title("AI-Based Aluminium Optimization System")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Total Heats",
        len(df)
    )

    c2.metric(
        "Average Al",
        round(df["Total_Al_kg"].mean(),1)
    )

    c3.metric(
        "Maximum Al",
        round(df["Total_Al_kg"].max(),1)
    )

    c4.metric(
        "Average Final Al",
        round(df["Final_AL"].mean(),4)
    )

    st.dataframe(df.head())