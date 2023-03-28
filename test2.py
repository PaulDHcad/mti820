import streamlit as st
import pandas as pd
import os
import hashlib

def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    credentials = read_credentials()
    if st.button("Log in"):
        if username in credentials:
            if verify_password(password, credentials[username]):
                st.success("Logged in as {}".format(username))
                return True
            else:
                st.warning("Incorrect password")
        else:
            st.warning("Username not found")
    if st.button("Create account"):
        create_account_page(credentials)
    return False

def read_credentials():
    if 'user_credentials.csv' not in os.listdir():
        return {}
    else:
        df = pd.read_csv('user_credentials.csv', index_col='username')
        return df['password'].to_dict()

def verify_password(password, hash):
    return hashlib.sha256(password.encode()).hexdigest() == hash

def create_account_page(credentials):
    st.header("Create Account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Create"):
        if new_username == "" or new_password == "":
            st.warning("Username or password is empty")
        elif new_username in credentials:
            st.warning("Username already exists")
        else:
            credentials[new_username] = hashlib.sha256(new_password.encode()).hexdigest()
            df = pd.DataFrame({'username': list(credentials.keys()), 'password': list(credentials.values())})
            df.to_csv('user_credentials.csv', index=False)
            st.success("Account created successfully!")
            st.info("Please log in to continue.")

def main():
    st.set_page_config(page_title="Login App")
    if not login_page():
        st.info("Please log in to continue.")

if __name__ == '__main__':
    main()
