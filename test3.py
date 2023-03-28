import streamlit as st
import pandas as pd
import hashlib

def signup():
    st.subheader("Create New Account")
    new_user = st.text_input("Enter Username")
    new_password = st.text_input("Enter Password", type="password")
    if st.button("Signup"):
        df = pd.read_csv("users.csv", index_col="Username")
        if new_user in df.index:
            st.warning("This username already exists. Please try again with a different username.")
        else:
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            df.loc[new_user] = [hashed_password]
            df.to_csv("users.csv")
            st.success("You have successfully created a new account. Please proceed to login.")
        return False
    else:
        return False

def login():
    st.subheader("Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        df = pd.read_csv("users.csv", index_col="Username")
        if username not in df.index:
            st.warning("This username does not exist. Please try again with a valid username.")
            return False
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == df.loc[username][0]:
                st.success("You have successfully logged in!")
                return True
            else:
                st.warning("Incorrect password. Please try again with a valid password.")
                return False
    else:
        return False

def main():
    st.title("My App")
    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to my app!")
    elif choice == "Login":
        if login():
            st.subheader("Home")
            st.write("Welcome to my app!")
    elif choice == "Signup":
        signup()

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import hashlib

def signup():
    st.subheader("Create New Account")
    new_user = st.text_input("Enter Username")
    new_password = st.text_input("Enter Password", type="password")
    if st.button("Signup"):
        df = pd.read_csv("users.csv", index_col="Username")
        if new_user in df.index:
            st.warning("This username already exists. Please try again with a different username.")
        else:
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            df.loc[new_user] = [hashed_password]
            df.to_csv("users.csv")
            st.success("You have successfully created a new account. Please proceed to login.")
        return False
    else:
        return False

def login():
    st.subheader("Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        df = pd.read_csv("users.csv", index_col="Username")
        if username not in df.index:
            st.warning("This username does not exist. Please try again with a valid username.")
            return False
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == df.loc[username][0]:
                st.success("You have successfully logged in!")
                return True
            else:
                st.warning("Incorrect password. Please try again with a valid password.")
                return False
    else:
        return False

def main():
    st.title("My App")
    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to my app!")
    elif choice == "Login":
        if login():
            st.subheader("Home")
            st.write("Welcome to my app!")
    elif choice == "Signup":
        signup()

if __name__ == "__main__":
    main()
