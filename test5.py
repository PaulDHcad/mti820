import streamlit as st
import csv
import os

def create_user_file():
    """Creates the user file if it doesn't exist"""
    if not os.path.exists("users.csv"):
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])

def add_user(username, password):
    """Adds a new user to the user file"""
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def check_user(username, password):
    """Checks if the username and password exist in the user file"""
    with open("users.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

def login():
    """Displays the login form and handles the login logic"""
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_user(username, password):
            st.success("Logged in!")
            return True
        else:
            st.error("Invalid username or password")
    return False

def signup():
    """Displays the sign up form and handles the sign up logic"""
    st.header("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        if password == confirm_password:
            add_user(username, password)
            st.success("Account created!")
            return True
        else:
            st.error("Passwords do not match")
    return False

def home():
    """Displays the home page"""
    st.header("Home")
    st.write("Welcome to the home page!")

def main():
    """Main function"""
    create_user_file()
    st.set_page_config(page_title="Login/Sign Up Example")
    st.title("Login/Sign Up Example")
    col1, col2 = st.beta_columns(2)
    if login():
        home()
    elif signup():
        login()
    else:
        home()

if __name__ == "__main__":
    main()
