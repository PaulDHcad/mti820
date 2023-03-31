import streamlit as st

def app():
    st.set_page_config(page_title="My App")

    button_clicked = st.button("Click me to start!")
    if button_clicked:
        st.write("Welcome to my app!")
