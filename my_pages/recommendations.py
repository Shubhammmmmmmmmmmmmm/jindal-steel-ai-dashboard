import streamlit as st

def app(df):

    st.title("📋 Recommendation Center")

    st.markdown("""
    Engineering recommendations generated from data analysis,
    feature importance study and AI model findings.
    """)

    st.divider()

    st.subheader("1️⃣ Optimize Final Aluminium Target")

    st.success("""
Expected Impact:
- Reduce excess aluminium additions
- Improve alloy recovery
- Lower production cost

Priority:
HIGH
""")

    st.divider()

    st.subheader("2️⃣ Reduce Process Time")

    st.warning("""
Expected Impact:
- Lower oxidation losses
- Better aluminium recovery
- Improved productivity

Priority:
HIGH
""")

    st.divider()

    st.subheader("3️⃣ Nitrogen Control")

    st.info("""
Expected Impact:
- Improved steel cleanliness
- Better process consistency
- Reduced aluminium consumption variation

Priority:
MEDIUM
""")

    st.divider()

    st.subheader("4️⃣ Grade-wise Aluminium Benchmarking")

    st.success("""
Expected Impact:
- Identify high consuming grades
- Establish consumption targets
- Reduce operator dependency

Priority:
HIGH
""")

    st.divider()

    st.subheader("5️⃣ AI-Based Recommendation System")

    st.error("""
Expected Impact:
- Real-time aluminium prediction
- Reduced human error
- Data-driven decision making

Priority:
VERY HIGH
""")

    st.divider()

    st.subheader("📈 Estimated Plant Benefits")

    st.markdown("""
### Potential Benefits

✅ 3–8 % Aluminium Saving

✅ Better Alloy Recovery

✅ Reduced Process Variation

✅ Standardized LRF Practice

✅ Lower Production Cost

✅ AI-Assisted Decision Making

✅ Industry 4.0 Digitalization

✅ Improved Process Control
""")