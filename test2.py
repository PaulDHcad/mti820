import streamlit as st
import pandas as pd
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_page():
    st.title("Login Page")
    st.write("---")
    st.write("Please enter your login credentials:")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if not (username and password):
            st.warning("Please fill in both fields.")
        else:
            df = pd.read_csv("user_credentials.csv")
            hashed_password = hash_password(password)
            if (df['Username']==username).any() and (df['Password']==hashed_password).any():
                st.success("Login successful!")
            else:
                st.warning("Incorrect username or password.")

def create_account_page(credentials):
    st.title("Create Account")
    st.write("---")
    st.write("Please enter your desired login credentials:")

    with st.form("create_account_form"):
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.form_submit_button("Create Account"):
            if not (new_username and new_password and confirm_password):
                st.warning("Please fill in all fields.")
            elif new_username in credentials.keys():
                st.warning("This username already exists. Please choose a different username.")
            elif new_password != confirm_password:
                st.warning("Passwords do not match. Please try again.")
            else:
                hashed_password = hash_password(new_password)
                credentials[new_username] = hashed_password
                df = pd.DataFrame.from_dict(credentials, orient="index", columns=["Password"])
                df.index.name = "Username"
                df.to_csv("user_credentials.csv")
                st.success("Account created successfully!")
                st.info("Please log in to your new account.")

def main():
    if 'user_credentials.csv' not in os.listdir():
        df = pd.DataFrame(columns=['Username', 'Password'])
        df.to_csv('user_credentials.csv', index=False)
    
    credentials = pd.read_csv("user_credentials.csv", index_col="Username").to_dict()["Password"]
    
    if not login_page():
        create_account_page(credentials)

if __name__ == '__main__':
    main()
