import streamlit as st
import pandas as pd
from hashlib import sha256
import os

USER_CREDS_FILE = "user_creds.csv"
HASH_ROUNDS = 100000


def hash_password(password, salt):
    return sha256((password + salt).encode()).hexdigest()


def create_user(username, password):
    salt = os.urandom(16).hex()
    hashed_password = hash_password(password, salt)
    df = pd.DataFrame({"Username": [username], "Salt": [salt], "HashedPassword": [hashed_password]})
    df.to_csv(USER_CREDS_FILE, mode="a", header=not os.path.exists(USER_CREDS_FILE), index=False)


def check_user_credentials(username, password):
    df = pd.read_csv(USER_CREDS_FILE)
    user_row = df.loc[df["Username"] == username]
    if user_row.empty:
        return False
    salt = user_row["Salt"].values[0]
    hashed_password = user_row["HashedPassword"].values[0]
    return hashed_password == hash_password(password, salt)


def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if check_user_credentials(username, password):
            st.success("Logged in!")
            return True, username
        else:
            st.warning("Incorrect username or password")
            return False, None


def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        df = pd.read_csv(USER_CREDS_FILE)
        if username in df["Username"].values:
            st.warning("Username already taken")
        else:
            create_user(username, password)
            st.success("Account created!")
            return True


def main():
    if not os.path.exists(USER_CREDS_FILE):
        pd.DataFrame({"Username": [], "Salt": [], "HashedPassword": []}).to_csv(USER_CREDS_FILE, index=False)

    st.set_page_config(page_title="Multi-Page App", page_icon=":guardsman:", layout="wide")

    st.title("Multi-Page App with Streamlit")

    menu = ["Login/Sign Up", "Home"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Login/Sign Up":
        if login()[0]:
            st.sidebar.success("Connected as {}".format(login()[1]))
            st.empty()
            st.stop()
        elif signup():
            st.sidebar.success("Connected as {}".format(signup()))
            st.empty()
            st.stop()
    elif choice == "Home":
        if not os.path.exists(USER_CREDS_FILE):
            st.warning("No users found. Please sign up first!")
            st.stop()
        else:
            if not st.session_state.get('logged_in', False):
                st.warning("You need to log in first!")
                st.stop()
            else:
                st.subheader("Home")
                st.write("Welcome to the Multi-Page App, {}".format(st.session_state['username']))
                if st.button("Disconnect"):
                    st.session_state['logged_in'] = False
                    st.sidebar.warning("Disconnected")
                    st.empty()
                    st.stop()

if __name__ == "__main__":
    main()
