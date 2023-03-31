import streamlit as st

def app():
    st.set_page_config(page_title="Home Page")

    if not st.session_state.get('button_clicked', False):
        if st.button('Click me'):
            st.session_state['button_clicked'] = True

    if st.session_state.get('button_clicked', False):
        st.write('Welcome to the home page!')
        # You can add your own content here
