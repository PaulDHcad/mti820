import streamlit as st
from streamlit_tags import st_tags
from streamlit_ace import st_ace

def home():
    st.title('Home Page')
    st.write('Welcome to my Streamlit app!')
    st.write('Use the sidebar to navigate to other pages.')

def editor():
    st.title('Editor Page')
    code = st_ace(value='', language='python', height=300)
    st.write('You entered the following code:')
    st.code(code)

def tags():
    st.title('Tags Page')
    tags = st_tags(
        label='Enter some tags:',
        text='Press enter to add more',
        value=['python', 'streamlit'],
        suggestions=['data science', 'machine learning', 'visualization']
    )
    st.write('You entered the following tags:')
    for tag in tags:
        st.write(tag)

# Define the pages dictionary
pages = {
    'Home': home,
    'Editor': editor,
    'Tags': tags
}

# Set the default page to 'Home'
default_page = 'Home'

# Create a sidebar with the page options
st.sidebar.title('Navigation')
selected_page = st.sidebar.radio('Go to', list(pages.keys()), index=list(pages.keys()).index(default_page))

# Display the selected page
pages[selected_page]()
