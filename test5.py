import streamlit as st

def signup_page():
    st.title("Sign Up")

    # Get user information
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Check if passwords match
    if password != confirm_password:
        st.error("Passwords do not match!")
        return

    # Check if user already exists
    with open("users.csv", "r") as f:
        for line in f:
            if email in line:
                st.error("User already exists!")
                return

    # Add new user to csv file
    with open("users.csv", "a") as f:
        f.write(f"{name},{email},{password}\n")

    st.success("User created!")

def login_page():
    st.title("Log In")

    # Get user information
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Check if user exists
    with open("users.csv", "r") as f:
        found = False
        for line in f:
            data = line.strip().split(",")
            if email == data[1] and password == data[2]:
                found = True
                break

    if found:
        st.success("Logged in!")
        st.write("Welcome to your Home Page")
    else:
        st.error("Invalid email or password")

def main():
    st.set_page_config(page_title="Sign Up / Log In Page")
    st.write("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 0.2, 2])
    with col1:
        signup_page()
    with col2:
        st.write("")
        st.write("")
        st.write("-- OR --")
        st.write("")
        st.write("")
    with col3:
        login_page()

if __name__ == "__main__":
    main()
