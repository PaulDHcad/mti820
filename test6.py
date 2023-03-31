import streamlit as st

def app():
    st.set_page_config(page_title="Button Example")

    button_clicked = st.button("Click Me!")

    if button_clicked:
        st.write("Button clicked! This is the home page.")
