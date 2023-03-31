import streamlit as st

def app():
    st.set_page_config(page_title="Example App", page_icon=":memo:", layout="wide")
    
    show_form = st.button("Show Form")
    
    if show_form:
        name = st.text_input("Enter your name:")
        age = st.slider("Enter your age:", 0, 100)
        submit = st.button("Submit")
        
        if submit:
            st.write(f"Your name is {name} and you are {age} years old.")
