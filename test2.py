import streamlit as st
import pandas as pd
import hashlib

USER_CREDS_FILE = "user_credentials.csv"
HASH_FUNCTION = hashlib.sha256

def create_account_page():
    st.header("Create New Account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if new_password != confirm_password:
        st.error("Error: Passwords do not match!")
        return

    # Hash the password and store the credentials
    hashed_password = HASH_FUNCTION(new_password.encode()).hexdigest()
    credentials = pd.read_csv(USER_CREDS_FILE, index_col="Username") if pd.read_csv(USER_CREDS_FILE, index_col="Username", error_bad_lines=False).empty == False else pd.DataFrame(columns=["Username", "Password"]).set_index("Username")
    if new_username in credentials.index:
        st.error("Error: Username already exists!")
        return
    credentials.loc[new_username] = [hashed_password]
    credentials.to_csv(USER_CREDS_FILE)
    st.success("Account created successfully!")
    st.info("Please login to your new account.")

def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    credentials = pd.read_csv(USER_CREDS_FILE, index_col="Username") if pd.read_csv(USER_CREDS_FILE, index_col="Username", error_bad_lines=False).empty == False else pd.DataFrame(columns=["Username", "Password"]).set_index("Username")
    if username in credentials.index:
        hashed_password = HASH_FUNCTION(password.encode()).hexdigest()
        if hashed_password == credentials.loc[username, "Password"]:
            st.success("Login successful!")
            return True
        else:
            st.error("Error: Incorrect password!")
    elif username != "":
        st.error("Error: Username not found!")
    return False

def home_page():
    st.header("Welcome to the Home Page")
    st.write("You are now logged in.")
    st.write("This is your home page.")

def main():
    st.set_page_config(page_title="Sign-In/Log-In", page_icon=":guardsman:", layout="wide")
    st.title("Sign-In/Log-In")

    # Create user credentials file if it doesn't exist
    try:
        pd.read_csv(USER_CREDS_FILE, index_col="Username")
    except FileNotFoundError:
        pd.DataFrame(columns=["Username", "Password"]).set_index("Username").to_csv(USER_CREDS_FILE)
    
    if not login_page():
        create_account_page()

    home_page()

if __name__ == "__main__":
    main()
