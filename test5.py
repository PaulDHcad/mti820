import streamlit as st

def add_user(username, password):
    with open("users.csv", "a") as f:
        f.write(f"{username},{password}\n")

def check_user(username, password):
    with open("users.csv", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                return True
        return False

def login_page():
    logged_in = st.session_state.get('logged_in', False)

    if not logged_in:
        col1, col2, col3 = st.columns([2, 0.1, 2])

        with col1:
            st.header("Sign Up")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Sign Up"):
                if username != "" and password != "":
                    add_user(username, password)
                    st.success("You have successfully signed up!")
                else:
                    st.warning("Please enter a username and password")

        with col2:
            st.write("|", width=10, )

        with col3:
            st.header("Log In")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Log In"):
                if check_user(username, password):
                    st.success("You have successfully logged in!")
                    st.session_state.logged_in = True
                else:
                    st.warning("Incorrect username or password")

    else:
        st.title("Welcome to the Home Page")
        st.write("You are now logged in!")
        st.write("This is the home page, where you can access all the features of our app.")


if __name__ == "__main__":
    login_page()
