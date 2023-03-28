import streamlit as st
import csv
import hashlib

def create_user_credentials_file():
    with open('user_credentials.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['email', 'hashed_password'])

def read_user_credentials_file():
    with open('user_credentials.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        return {row[0]: row[1] for row in reader}

def write_user_credentials(email, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open('user_credentials.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([email, hashed_password])

def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Log in"):
        user_credentials = read_user_credentials_file()
        if email in user_credentials and \
                user_credentials[email] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            st.success("Logged in as {}".format(email))
            return True
        else:
            st.error("Incorrect email or password")
    return False

def signup_page():
    st.title("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        if password == confirm_password:
            write_user_credentials(email, password)
            st.success("Successfully created account for {}".format(email))
            return True
        else:
            st.error("Passwords do not match")
    return False

def home_page():
    st.title("Welcome")
    st.write("You are now logged in.")

def main():
    if 'user_credentials.csv' not in os.listdir():
        create_user_credentials_file()

    login = False
    signup = False

    if st.sidebar.button("Log in"):
        login = login_page()

    if st.sidebar.button("Sign Up"):
        signup = signup_page()

    if login or signup:
        home_page()

if __name__ == "__main__":
    main()
