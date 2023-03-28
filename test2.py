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
