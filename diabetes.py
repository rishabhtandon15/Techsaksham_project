import streamlit as st

def app():
    st.title("Diabetes Prediction")
    with st.expander("About Diabetes Prediction"):
        st.write(
            """
            This tool predicts the likelihood of diabetes based on factors such as pregnancies, glucose level, and BMI.
            """
        )

    # Input fields (Replace with your actual features)
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=300, step=1)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)

    with col2:
        insulin = st.number_input("Insulin Level", min_value=0, max_value=800, step=1)
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, step=0.1)
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, step=0.01)
        age = st.number_input("Age", min_value=0, max_value=150, step=1)

    if st.button("Predict Diabetes"):
        # **REPLACE WITH YOUR DIABETES PREDICTION LOGIC**
        # Load model, scaler, make prediction
        prediction = 0  # Placeholder!
        if prediction == 0:
            st.success("The model predicts: No Diabetes")
        else:
            st.error("The model predicts: Diabetes")