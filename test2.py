import streamlit as st

def home():
    st.title('Home Page')
    st.write('Welcome to my Streamlit app!')
    st.write('Use the sidebar to navigate to other pages.')

def editor():
    st.title('Editor Page')
    code = st.text_area('Enter some code:')
    st.write('You entered the following code:')
    st.code(code)

def tags():
    st.title('Tags Page')
    tags = st.text_input('Enter some tags (separated by commas):')
    st.write('You entered the following tags:')
    for tag in tags.split(','):
        st.write(tag.strip())

def sign_in():
    st.title('Sign In')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Sign In'):
        # Do sign-in logic here
        st.write('You have signed in.')

def log_in():
    st.title('Log In')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Log In'):
        # Do log-in logic here
        st.write('You have logged in.')

# Define the pages dictionary
pages = {
    'Home': home,
    'Editor': editor,
    'Tags': tags,
    'Sign In': sign_in,
    'Log In': log_in
}

# Set the default page to 'Home'
default_page = 'Home'

# Create a sidebar with the page options
st.sidebar.title('Navigation')
for page_name in pages.keys():
    if page_name == default_page:
        st.sidebar.write(f'**{page_name}**')
    else:
        st.sidebar.write(f'[{page_name}](#{page_name.lower().replace(" ", "-")})')

# Display the selected page
selected_page = st.sidebar.selectbox('', list(pages.keys()), index=list(pages.keys()).index(default_page))
st.sidebar.write('---')
st.sidebar.write(f'You are currently on the **{selected_page}** page.')

pages[selected_page]()
