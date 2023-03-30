import streamlit as st
import csv
import os

def create_csv():
    # create csv file if it doesn't exist
    if not os.path.exists('users.csv'):
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])

def add_user(username, password):
    # add new user to the csv file
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def check_credentials(username, password):
    # check if the given credentials match any user in the csv file
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
        return False

def login():
    st.subheader("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if check_credentials(username, password):
            st.success("Logged in as {}".format(username))
            hide_menu()
        else:
            st.error("Invalid username or password")

def sign_up():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        add_user(username, password)
        st.success("Account created for {}".format(username))

def hide_menu():
    # hide the login and sign up pages and show the home page
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.subheader("Home")
    st.write("Welcome to the home page")

create_csv()

menu = ["Home", "Log In", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Log In":
    login()
elif choice == "Sign Up":
    sign_up()
else:
    hide_menu()
