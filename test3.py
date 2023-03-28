import streamlit as st
import pandas as pd
import hashlib

def login():
    st.title("Login")
    df = pd.read_csv("users.csv")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if (df["Username"] == username).any() and (df["Password"] == hashed_password).any():
            st.success("Logged in!")
            return True
        else:
            st.error("Invalid username or password.")
    return False

def signup():
    st.title("Sign Up")
    df = pd.read_csv("users.csv", index_col=0)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if username in df.index:
            st.error("This username already exists.")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            df.loc[username, "Password"] = hashed_password
            df.to_csv("users.csv")
            st.success("You have successfully created a new account.")
            return True
    return False

def main():
    if login():
        st.title("Home")
        st.write("Welcome to the home page.")
    else:
        if signup():
            st.title("Login")
            st.info("Please log in with your new account.")
        else:
            st.title("Sign Up")
            st.info("Please create a new account.")
            
if __name__ == "__main__":
    main()
