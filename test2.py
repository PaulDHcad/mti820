import streamlit as st
import pandas as pd
import hashlib

def login_page():
    st.title("Sign-in / Log-in")
    
    if "user_credentials.csv" not in st.session_state:
        st.session_state.user_credentials = pd.DataFrame(columns=["Username", "Password"])

    credentials = st.session_state.user_credentials.set_index("Username")["Password"].to_dict()
    
    if not credentials:
        st.warning("User credentials file is missing or empty.")
        st.session_state.user_credentials = pd.DataFrame(columns=["Username", "Password"])
        return False
    
    login_form = st.form("login_form")
    
    with login_form:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Log in")
        
        if submit:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            if username in credentials and credentials[username] == hashed_password:
                st.success("You have successfully logged in!")
                return True
            else:
                st.error("Incorrect username or password.")
    
    signup_form = st.form("signup_form")
    
    with signup_form:
        st.header("Create a new account")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Create account")
        
        if submit:
            if new_username in credentials:
                st.error("Username already exists.")
            else:
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                st.session_state.user_credentials = st.session_state.user_credentials.append({"Username": new_username, "Password": hashed_password}, ignore_index=True)
                st.success("Account created successfully!")
    
    return False


def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")


def main():
    if not login_page():
        return
    
    home_page()

if __name__ == "__main__":
    main()
