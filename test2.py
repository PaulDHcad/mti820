import streamlit as st
import csv

USER_STORAGE_FILE = 'users.csv'

# If the user storage file doesn't exist, create an empty file
if not os.path.isfile(USER_STORAGE_FILE):
    with open(USER_STORAGE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["email", "password"])

def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("You are logged in.")

def login_page():
    st.title("Login Page")
    st.write("Please enter your login credentials.")
    
    # Read the existing user credentials from the CSV file
    with open(USER_STORAGE_FILE, 'r') as f:
        reader = csv.reader(f)
        user_credentials = {rows[0]:rows[1] for rows in reader}
        
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Log in"):
        # Check if the user entered a valid email and password
        if email in user_credentials and user_credentials[email] == password:
            st.success("You have successfully logged in!")
            # Redirect the user to the home page after logging in
            st.experimental_rerun()
        else:
            st.error("Invalid login credentials.")

def main():
    # Set the page title and icon
    st.set_page_config(page_title="Multi-Page App Example", page_icon=":memo:")
    
    # Create a session state variable to keep track of whether the user is logged in
    if "loggedin" not in st.session_state:
        st.session_state.loggedin = False
    
    # Display the appropriate page based on whether the user is logged in
    if st.session_state.loggedin:
        home_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
