import streamlit as st

# Define the Streamlit app
def app():
    st.set_page_config(page_title="Button Example")

    # Create a button
    button_clicked = st.button("Click me!")

    # Check if the button has been clicked
    if button_clicked:
        # Display a message
        st.write("Button clicked!")
