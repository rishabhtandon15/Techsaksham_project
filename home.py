import streamlit as st

def app():
    st.title("Welcome to the Disease Prediction Platform")
    st.markdown(
        """
        This platform provides tools to predict the likelihood of various diseases based on user-provided health information.

        **Important Disclaimer:** The predictions made here are for informational purposes only and should not be considered medical diagnoses. Always consult with a qualified healthcare professional for any health concerns.

        To begin, please select a disease from the sidebar menu.
        """
    )

    st.subheader("Key Features")
    st.markdown(
        """
        -   **Multiple Disease Predictions:** Predict the likelihood of Diabetes, Hypothyroid, Parkinson's, and Lung Cancer.
        -   **User-Friendly Interface:** Easy-to-use input forms to provide health information.
        -   **Interactive Results:** Clear and concise prediction results.
        """
    )
    st.image("home_page_image.png") # Replace with your image