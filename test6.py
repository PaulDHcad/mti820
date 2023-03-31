import streamlit as st

def home():
    st.write("Welcome to the home page!")
    # You can add your own content here

def app():
    st.set_page_config(page_title="My Streamlit App")

    # Create a button to show the home page
    if st.button("Show Home Page"):
        home()

    # Show the initial button if the home page is not displayed yet
    if not st.session_state.get("home_displayed", False):
        st.write("Press the button below to show the home page")
    else:
        st.session_state.home_displayed = True
