import streamlit as st

# Create a boolean variable to control the visibility of the form
show_form = True

# Define the Streamlit app
def app():
    st.set_page_config(page_title="Hiding Form Example", page_icon=":eyes:", layout="wide")

    # Create a form
    if show_form:
        name = st.text_input("Enter your name")
        age = st.slider("Enter your age", 0, 100, 25)
        if st.button("Submit"):
            # Do something with the form data
            st.write("Name:", name)
            st.write("Age:", age)
            # Hide the form by setting the boolean variable to False
            show_form = False

    # Show a message after the form is hidden
    if not show_form:
        st.write("Thanks for submitting the form!")
