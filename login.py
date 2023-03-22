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

# Add a title
st.title("Login or Sign Up")

# Add radio buttons to select login or sign up
choice = st.radio("Select an action", ("Login", "Sign Up"))

# If the user selects sign up
if choice == "Sign Up":
    # Add user input fields for username, password, and email
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    new_email = st.text_input("Email")

    # Add a button to submit the sign up information
    if st.button("Sign Up"):
        if username_exists(new_username):
            st.error("Username already taken")
        else:
            add_user(new_username, new_password, new_email)
            st.success("Successfully signed up")

# If the user selects login
elif choice == "Login":
    # Add user input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Add a button to submit the login credentials
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Logged in as {}".format(username))
            # Add the rest of your application logic here
        else:
            st.error("Incorrect username or password")
