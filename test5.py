import streamlit as st
import csv
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
from streamlit.hashing import _CodeHasher

# Create a function to read user credentials from the CSV file
def read_user_data():
    with open('user_credentials.csv', 'r') as f:
        reader = csv.reader(f)
        user_data = list(reader)
    return user_data

# Create a function to write user credentials to the CSV file
def write_user_data(username, password):
    with open('user_credentials.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

# Define the Streamlit app
def app():
    st.set_page_config(page_title="Sign-up/Login Page", page_icon=":guardsman:", layout="wide")
    
    # Create a session state to persist the logged-in state across app sessions
    class SessionState:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    session_state = SessionState(logged_in=False)
    
    # Define the layout for the sign-up and login forms
    col1, col2, col3 = st.beta_columns([1, 0.1, 1])

    with col1:
        st.write('Sign Up')
        # Create input fields for new username and password
        new_username = st.text_input('New Username')
        new_password = st.text_input('New Password', type='password')

        # Create a button to sign up
        if st.button('Sign Up'):
            # Check if username and password fields are not empty
            if new_username and new_password:
                # Read existing user data from the CSV file
                user_data = read_user_data()
                # Check if the username already exists in the CSV file
                usernames = [user[0] for user in user_data]
                if new_username in usernames:
                    st.error('Username already exists. Please choose a different one.')
                else:
                    # Write the new user credentials to the CSV file
                    write_user_data(new_username, new_password)
                    st.success('Successfully signed up. Please log in.')
            else:
                st.error('Please enter a username and password.')

    with col2:
        # Add a vertical bar between the two columns
        st.markdown('<hr style="border: none; border-left: 1px solid #ccc; height: 800px;">', unsafe_allow_html=True)

    with col3:
        st.write('Log In')
        # Create input fields for existing username and password
        existing_username = st.text_input('Existing Username')
        existing_password = st.text_input('Existing Password', type='password')

        # Create a button to log in
        if st.button('Log In'):
            # Check if username and password fields are not empty
            if existing_username and existing_password:
                # Read existing user data from the CSV file
                user_data = read_user_data()
                # Check if the username and password match any of the credentials in the CSV file
                for user in user_data:
                    if existing_username == user[0] and existing_password == user[1]:
                        session_state.logged_in = True
                        st.success('Successfully logged in
