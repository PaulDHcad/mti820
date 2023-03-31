import streamlit as st

def app():
    st.set_page_config(page_title="Welcome", page_icon=":guardsman:", layout="wide")

    # Display the button
    button_pressed = st.button("Click me to start")

    # If the button is pressed, display the welcome message
    if button_pressed:
        st.write("Welcome to my Streamlit app!")
