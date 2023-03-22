import streamlit as st

# Define the correct username and password for login
CORRECT_USERNAME = 'myusername'
CORRECT_PASSWORD = 'mypassword'

# Define an empty dictionary to store user information
user_info = {}

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
        if new_username in user_info:
            st.error("Username already taken")
        else:
            user_info[new_username] = {'password': new_password, 'email': new_email}
            st.success("Successfully signed up")

# If the user selects login
elif choice == "Login":
    # Add user input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Add a button to submit the login credentials
    if st.button("Login"):
        if username in user_info:
            if password == user_info[username]['password']:
                st.success("Logged in as {}".format(username))
                # Add the rest of your application logic here
            else:
                st.error("Incorrect password")
        else:
            st.error("User does not exist")
