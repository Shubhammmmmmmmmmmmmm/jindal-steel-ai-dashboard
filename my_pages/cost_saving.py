import streamlit as st

def app(df):

    st.title("💰 Cost Saving Analysis")

    st.markdown("""
    Estimate potential savings from Aluminium Consumption Optimization.
    """)

    col1, col2 = st.columns(2)

    with col1:

        al_price = st.number_input(
            "Aluminium Price (₹/kg)",
            value=250.0
        )

    with col2:

        saving_percent = st.slider(
            "Target Saving (%)",
            1,
            20,
            5
        )

    avg_al = df["Total_Al_kg"].mean()

    saving_kg = avg_al * saving_percent / 100

    saving_per_heat = saving_kg * al_price

    daily_saving = saving_per_heat * 30

    monthly_saving = daily_saving * 30

    annual_saving = daily_saving * 365

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Saving/Heat",
        f"₹ {saving_per_heat:,.0f}"
    )

    c2.metric(
        "Daily Saving",
        f"₹ {daily_saving:,.0f}"
    )

    c3.metric(
        "Monthly Saving",
        f"₹ {monthly_saving:,.0f}"
    )

    c4.metric(
        "Annual Saving",
        f"₹ {annual_saving:,.0f}"
    )

    st.divider()

    st.success(f"""
### Estimated Benefit

Current Average Aluminium Consumption:
**{avg_al:.2f} kg/heat**

Target Saving:
**{saving_percent}%**

Potential Aluminium Reduction:
**{saving_kg:.2f} kg/heat**

Estimated Annual Saving:
**₹ {annual_saving:,.0f}**
""")