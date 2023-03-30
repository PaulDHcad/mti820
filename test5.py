import streamlit as st
import pandas as pd
import os

# Set up page layout
st.set_page_config(page_title="Login/Sign up", page_icon=":guardsman:", layout="wide")

# Define login function
def login(df, username, password):
    # Check if username exists in dataframe
    if username not in df['Username'].tolist():
        st.error("Invalid username")
        return False
    # Check if password matches for given username
    if df.loc[df['Username'] == username, 'Password'].iloc[0] != password:
        st.error("Incorrect password")
        return False
    st.success("Logged in successfully!")
    return True

# Define sign up function
def sign_up(df, username, password):
    # Check if username already exists in dataframe
    if username in df['Username'].tolist():
        st.error("Username already exists")
        return False
    # Add new user to dataframe
    new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv('user_credentials.csv', index=False)
    st.success("Signed up successfully!")
    return True

# Define main function
def main():
    # Create user credentials CSV file if it doesn't exist
    if not os.path.exists('user_credentials.csv'):
        pd.DataFrame({'Username': [], 'Password': []}).to_csv('user_credentials.csv', index=False)

    # Load user credentials CSV file into dataframe
    df = pd.read_csv('user_credentials.csv')

    # Define login and sign up form inputs
    with st.sidebar:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Log in")
        
        st.title("Sign up")
        new_username = st.text_input("New username")
        new_password = st.text_input("New password", type="password")
        sign_up_button = st.button("Sign up")

    # Handle login and sign up form submissions
    if login_button:
        if login(df, username, password):
            st.experimental_rerun()
    if sign_up_button:
        if sign_up(df, new_username, new_password):
            st.experimental_rerun()

    # Hide login and sign up form and show home page if user is logged in
    if 'logged_in' not in st.session_state:
        st.title("Home page")
        st.write("Welcome to the home page! Please log in or sign up to continue.")
    else:
        st.title("Logged in as: " + st.session_state['logged_in'])
        st.write("This is the home page for logged in users.")

        # Add logout button
        logout_button = st.button("Log out")
        if logout_button:
            st.session_state.pop('logged_in')
            st.experimental_rerun()

    # Set logged_in session state variable if user successfully logs in
    if login_button and login(df, username, password):
        st.session_state['logged_in'] = username

if __name__ == '__main__':
    main()
