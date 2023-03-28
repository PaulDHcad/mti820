import streamlit as st
import pandas as pd

def login_page():
    st.title("Login Page")

    credentials = None

    if st.button("Create new account"):
        create_account_page()
    elif st.button("Login"):
        credentials = get_login_credentials()

    return credentials

def create_account_page():
    st.title("Create Account")

    credentials = get_login_credentials()

    if credentials:
        df = pd.DataFrame.from_dict(credentials, orient="index", columns=["Password"])
    else:
        df = pd.DataFrame(columns=["Password"])

    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    new_password_confirm = st.text_input("Confirm Password", type="password")

    if new_password != new_password_confirm:
        st.error("Passwords do not match")
    elif new_username in df.index:
        st.error("Username already exists")
    elif st.button("Create Account"):
        df.loc[new_username] = new_password
        df.to_csv("user_credentials.csv", index_label="Username")
        st.success("Account created successfully!")

def get_login_credentials():
    try:
        credentials = pd.read_csv("user_credentials.csv", index_col="Username")
        if set(credentials.columns) != set(["Password"]):
            raise ValueError("User credentials file is missing required columns.")
    except FileNotFoundError:
        credentials = None

    return credentials

def main():
    st.set_page_config(page_title="Login App")

    if not login_page():
        st.error("Incorrect username or password")

if __name__ == "__main__":
    main()
