import streamlit as st
import pandas as pd
import hashlib
import os

# Constants
USER_CREDS_FILE = "user_credentials.csv"
HASH_SALT = "5gz"
HOME = "Home"
SIGN_UP = "Sign up"
LOG_IN = "Log in"
LOG_OUT = "Log out"


def hash_password(password):
    return hashlib.sha256(f"{password}{HASH_SALT}".encode()).hexdigest()


def create_user_credentials_file():
    df = pd.DataFrame(columns=["Username", "Password"])
    df.to_csv(USER_CREDS_FILE, index=False)


def authenticate_user(username, password):
    df = pd.read_csv(USER_CREDS_FILE)
    hashed_password = hash_password(password)
    if username in df["Username"].values and hashed_password in df["Password"].values:
        return True
    return False


def signup():
    st.subheader("Create a new account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign up"):
        hashed_password = hash_password(password)
        df = pd.read_csv(USER_CREDS_FILE)
        if username in df["Username"].values:
            st.error("Username already exists")
        else:
            df = df.append({"Username": username, "Password": hashed_password}, ignore_index=True)
            df.to_csv(USER_CREDS_FILE, index=False)
            st.success("Account created successfully")


def login():
    st.subheader("Please log in")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log in"):
        if authenticate_user(username, password):
            st.success("Logged in successfully")
            return True
        else:
            st.error("Invalid username or password")
    return False


def main():
    st.set_page_config(page_title="Secure App", page_icon="🔒")
    
    if not os.path.isfile(USER_CREDS_FILE):
        create_user_credentials_file()
    
    st.sidebar.title("Navigation")
    nav_item = st.sidebar.radio("", [LOG_IN, SIGN_UP])
    
    if nav_item == SIGN_UP:
        signup()
    elif nav_item == LOG_IN:
        if login():
            st.sidebar.title("Welcome")
            st.sidebar.success("Logged in successfully")
            st.sidebar.button(LOG_OUT)
            st.header(HOME)
        else:
            st.header(LOG_IN)


if __name__ == "__main__":
    main()
