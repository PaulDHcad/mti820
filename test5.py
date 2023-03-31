import csv
import streamlit as st

def signup_page():
    st.header("Sign Up")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Sign Up"):
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        st.success("You have successfully created an account!")

def login_page():
    st.header("Log In")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Log In"):
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    st.success("You have successfully logged in!")
                    return True
        st.warning("Incorrect username or password.")
    return False

def main():
    st.set_page_config(page_title="My App", page_icon=":guardsman:", layout="wide")
    col1, col2, col3 = st.beta_columns([1, 0.1, 1])
    with col1:
        if not login_page():
            signup_page()
    with col2:
        st.write("")
        st.write("---OR---")
        st.write("")
    with col3:
        if not login_page():
            signup_page()

    if login_page():
        st.write("")
        st.write("---Home Page---")
        # Add your home page content here

if __name__ == "__main__":
    main()
