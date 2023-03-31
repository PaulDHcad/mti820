import streamlit as st

# Define function for login page
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check if username and password are correct
        if username == "myuser" and password == "mypassword":
            st.success("Login successful!")
            # Redirect to home page
            return "home"
        else:
            st.error("Invalid username or password")

# Define function for home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("This is a sample app with multiple pages.")

# Define dictionary of pages
pages = {
    "login": login,
    "home": home,
}

# Set initial page to login
current_page = "login"

# Loop until user logs in
while current_page == "login":
    # Run current page function
    current_page_func = pages[current_page]
    current_page = current_page_func()

# Once user logs in, show home page
if current_page == "home":
    home()
