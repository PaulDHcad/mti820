import streamlit as st
import hashlib
import os

# Define the path to the user storage file
USER_STORAGE_FILE = 'users.txt'

# If the user storage file doesn't exist, create an empty file
if not os.path.isfile(USER_STORAGE_FILE):
    with open(USER_STORAGE_FILE, 'w') as f:
        pass

# Define a function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define a function to check if a username exists in the user storage file
def username_exists(username):
    with open(USER_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_username, _, _ = line.strip().split(',')
            if username == stored_username:
                return True
    return False

# Define a function to add a new user to the user storage file
def add_user(username, password, email):
    with open(USER_STORAGE_FILE, 'a') as f:
        f.write('{},{},{}\n'.format(username, hash_password(password), email))

# Define a function to check if the login credentials are correct
def check_credentials(username, password):
    with open(USER_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_username, stored_password, _ = line.strip().split(',')
            if username == stored_username and hash_password(password) == stored_password:
                return True
    return False

# Define a function to get the user's email
def get_user_email(username):
    with open(USER_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_username, _, stored_email = line.strip().split(',')
            if username == stored_username:
                return stored_email
    return None

# Add a title to the app
st.title("Welcome to the Login/Sign Up Page")

# Add two buttons to the landing page for login and sign up
if st.button("Login"):
    # Add user input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Add a button to submit the login credentials
    if st.button("Submit"):
        if check_credentials(username, password):
            st.success("Logged in as {}".format(username))
            st.write("Your email is:", get_user_email(username))
        else:
            st.error("Incorrect username or password")

if st.button("Sign Up"):
    # Add user input fields for username, password, and email
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")

    # Add a button to submit the sign up information
    if st.button("Submit"):
        if username_exists(username):
            st.error("Username already taken")
        else:
            add_user(username, password, email)
            st.success("Successfully signed up")

