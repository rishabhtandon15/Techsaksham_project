import streamlit as st
import home
import diabetes
import hypothyroid
import parkinson
import pre_hypothyroid
import pre_lungs
import lung_cancer
import auth
import utils  # Import utility functions

def main():
    st.set_page_config(page_title="Disease Prediction Platform", page_icon=":heartpulse:")
    utils.local_css("style.css")  # Apply custom CSS

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['show_signup'] = False  # Track signup mode

    if not st.session_state['logged_in']:
        if not st.session_state['show_signup']:
            # Login Form
            st.title("Welcome to the Disease Prediction Platform")
            #st.image("medical_image.png", width=300)  # REMOVED: Requires the image file
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Login"):
                    if auth.authenticate_user(username, password):  # Use auth.py
                        st.session_state['logged_in'] = True
                        st.success("Logged in successfully!")
                        st.rerun()  # Refresh to show main app
                    else:
                        st.error("Incorrect username or password")
            with col2:
                if st.button("Signup"):
                    st.session_state['show_signup'] = True
                    st.rerun()  # Refresh to show signup form
        else:
            # Signup Form
            st.title("Create an Account")
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            col1, col2 = st.columns(2)  # Create columns for Signup and Back to Login
            with col1:
                if st.button("Signup"):
                    if auth.signup_user(new_username, new_password):  # Use auth.py
                        st.success("Account created! Please log in.")
                        st.session_state['show_signup'] = False
                        st.rerun()  # Go back to login
                    else:
                        st.error("Username already exists. Choose a different one.")
            with col2:
                if st.button("Back to Login"):
                    st.session_state['show_signup'] = False
                    st.rerun()  # Go back to login
    else:
        # Main App - Navigation
        with st.sidebar:
            st.title("Disease Prediction")
            app_mode = st.selectbox(
                "Choose the prediction type",
                [
                    "Home",
                    "Diabetes",
                    "Hypothyroid",
                    "Parkinson",
                    "Preprocessed Hypothyroid",
                    "Preprocessed Lungs",
                    "Lung Cancer",
                ],
            )
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.rerun()  # Force a refresh to show login

        # Page Routing
        if app_mode == "Home":
            home.app()
        elif app_mode == "Diabetes":
            diabetes.app()
        elif app_mode == "Hypothyroid":
            hypothyroid.app()
        elif app_mode == "Parkinson":
            parkinson.app()
        elif app_mode == "Preprocessed Hypothyroid":
            pre_hypothyroid.app()
        elif app_mode == "Preprocessed Lungs":
            pre_lungs.app()
        elif app_mode == "Lung Cancer":
            lung_cancer.app()

if __name__ == '__main__':
    main()