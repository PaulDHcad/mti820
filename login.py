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
            stored_username, _, _, _ = line.strip().split(',')
            if username == stored_username:
                return True
    return False

# Define a function to add a new user to the user storage file
def add_user(username, password, email, location):
    with open(USER_STORAGE_FILE, 'a') as f:
        f.write('{},{},{},{}\n'.format(username, hash_password(password), email, location))

# Define a function to check if the login credentials are correct
def check_credentials(username, password):
    with open(USER_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_username, stored_password, _, _ = line.strip().split(',')
            if username == stored_username and hash_password(password) == stored_password:
                return True
    return False

# Define a function to get the user's location
def get_user_location(username):
    with open(USER_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_username, _, _, location = line.strip().split(',')
            if username == stored_username:
                return location
    return None

# Add a title
st.title("Login or Sign Up")

# Add user input fields for username, password, email, and location
username = st.text_input("Username")
password = st.text_input("Password", type="password")
email = st.text_input("Email")
location = st.text_input("Location")

# Add radio buttons to select login or sign up
choice = st.radio("Select an action", ("Login", "Sign Up"))

# If the user selects sign up
if choice == "Sign Up":
    # Add a button to submit the sign up information
    if st.button("Sign Up"):
        if username_exists(username):
            st.error("Username already taken")
        else:
            add_user(username, password, email, location)
            st.success("Successfully signed up")

# If the user selects login
elif choice == "Login":
    # Add a button to submit the login credentials
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Logged in as {}".format(username))

            # If this is the user's first login, ask for movie type preferences
            if get_user_location(username) is None:
                st.info("Please select your preferred movie types")
                movie_types = st.multiselect("Select one or more movie types", ["Action", "Comedy", "Drama", "Horror"])
                if len(movie_types) > 0:
                    st.success("Movie types saved")
                    # Add the user's location and movie type preferences to the user storage file
                    with open(USER_STORAGE_FILE, 'r') as f:
                        lines = f.readlines()
                    with open(USER_STORAGE_FILE, 'w') as f:
                        for line in lines:
                            stored_username, stored_password, stored_email,
