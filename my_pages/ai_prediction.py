import joblib

model = joblib.load(
    "Output/RF_Al_Model.pkl"
)
if st.button(
"Predict Aluminium Requirement"
):

    pred = model.predict([[
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

        LIFTING_TEMERATURE,
        PROCESS_TIME,

        POWER_y,
        HM,
        DRI,
        LIME_y,
        DOLO,
        CPC
    ]])

    st.success(
        f"Predicted Aluminium = {pred[0]:.1f} kg"
    )
    