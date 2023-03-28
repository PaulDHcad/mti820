import streamlit as st

# Define your Streamlit pages as functions
def page_home():
    st.title("Welcome to my app!")
    # Add any other content you want on this page

def page_about():
    st.title("About me")
    # Add any other content you want on this page

# Define a dictionary that maps page names to their corresponding functions
PAGES = {
    "Home": page_home,
    "About": page_about
}

# Set up the sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Call the function corresponding to the selected page name
PAGES[page]()
