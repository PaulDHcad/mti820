import os
import hashlib
import pandas as pd
import streamlit as st


def hash_password(password):
    """Hashes a password using SHA-256 algorithm."""
    return hashlib.sha256(password.encode()).hexdigest()


def login_page():
    """Displays the login page and handles user authentication."""
    st.header("Login")

    # Get username and password from user
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Load user credentials from CSV file
    credentials = pd.read_csv(get_file_path())

    # Check if username and hashed password match
    if st.button("Login"):
        hashed_password = hash_password(password)
        if (credentials["username"] == username).any() and \
           (credentials["password"] == hashed_password).any():
            st.success("Logged in!")
            return True
        else:
            st.error("Incorrect username or password.")

    # Show "Create account" button
    if st.button("Create account"):
        create_account_page(credentials)
    return False


def create_account_page(credentials):
    """Displays the create account page and handles account creation."""
    st.header("Create account")

    # Get username and password from user
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    # Check if passwords match
    if password != confirm_password:
        st.error("Passwords do not match.")
        return

    # Check if username already exists
    if (credentials["username"] == username).any():
        st.error("Username already exists.")
        return

    # Add new user to CSV file
    hashed_password = hash_password(password)
    new_user = pd.DataFrame({"username": [username], "password": [hashed_password]})
    credentials = pd.concat([credentials, new_user])
    credentials.to_csv(get_file_path(), index=False)

    st.success("Account created!")
    return


def home_page():
    """Displays the home page for authenticated users."""
    st.header("Home page")
    st.write("Welcome to the home page.")


def get_file_path():
    """Returns the absolute path of the CSV file."""
    file_name = "user_credentials.csv"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    return file_path


def main():
    # Check if CSV file exists, otherwise create it
    file_path = get_file_path()
    if not os.path.isfile(file_path):
        pd.DataFrame({"username": [], "password": []}).to_csv(file_path, index=False)

    # Check if user is logged in
    if not login_page():
        return

    # Show home page
    home_page()


if __name__ == "__main__":
    main()
