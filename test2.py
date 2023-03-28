import os
import pandas as pd
import streamlit as st
from passlib.hash import pbkdf2_sha256

USER_CREDS_FILE = "user_credentials.csv"
EXPECTED_COLUMNS = ["Username", "Password"]


def get_user_credentials():
    if not os.path.isfile(USER_CREDS_FILE):
        create_user_credentials_file()

    df = pd.read_csv(USER_CREDS_FILE, index_col="Username")

    # Verify that the expected columns are present in the user credentials file
    if set(df.columns) != set(EXPECTED_COLUMNS):
        raise ValueError("User credentials file is missing required columns.")

    return df.to_dict()["Password"]


def create_user_credentials_file():
    df = pd.DataFrame(columns=EXPECTED_COLUMNS)
    df.to_csv(USER_CREDS_FILE, index=False)


def main():
    st.set_page_config(page_title="Login", page_icon=":guardsman:", layout="wide")

    # Get user credentials
    credentials = get_user_credentials()

    # Login form
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Verify user credentials
        if username in credentials and pbkdf2_sha256.verify(password, credentials[username]):
            st.success("Logged in!")
        else:
            st.error("Invalid username or password")


if __name__ == "__main__":
    main()
