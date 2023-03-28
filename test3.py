import streamlit as st
import pandas as pd
import hashlib

USER_CREDS_FILE = "user_credentials.csv"

def login():
    st.write("## Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        df = pd.read_csv(USER_CREDS_FILE, index_col="Username")
        if username in df.index:
            if hashlib.sha256(password.encode()).hexdigest() == df.loc[username, "Password"]:
                st.success("Logged in!")
                return True
            else:
                st.error("Invalid password")
        else:
            st.error("Username not found")
    return False

def signup():
    st.write("## Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        try:
            df = pd.read_csv(USER_CREDS_FILE, index_col="Username")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Username", "Password"])
        
        if username in df.index:
            st.error("Username already taken")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            df.loc[username] = [hashed_password]
            df.to_csv(USER_CREDS_FILE)
            st.success("Successfully created account")
            return True
    return False

def home():
    st.write("## Welcome to the Home Page!")
    st.write("This is the home page")

def main():
    if not st.sidebar.checkbox("Login", False):
        if signup():
            st.sidebar.success("Account created! Please login.")
        return
    elif login():
        home()

if __name__ == "__main__":
    main()
