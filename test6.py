import streamlit as st

def app():
    st.set_page_config(page_title="Sign-up/Login Page", page_icon=":guardsman:", layout="wide")

    # Create a boolean variable to keep track of login status
    logged_in = False

    # Define the layout for the sign-up and login forms
    col1, col2, col3 = st.beta_columns([1, 0.1, 1])

    with col1:
        st.write('Sign Up')
        # Create input fields for new username and password
        new_username = st.text_input('New Username')
        new_password = st.text_input('New Password', type='password')

        # Create a button to sign up
        if st.button('Sign Up'):
            # Check if username and password fields are not empty
            if new_username and new_password:
                # Write the new user credentials to a text file
                with open('user_credentials.txt', 'a') as f:
                    f.write(f"{new_username},{new_password}\n")
                st.success('Successfully signed up. Please log in.')
            else:
                st.error('Please enter a username and password.')

    with col2:
        # Add a vertical bar between the two columns
        st.markdown('<hr style="border: none; border-left: 1px solid #ccc; height: 800px;">', unsafe_allow_html=True)

    with col3:
        st.write('Log In')
        # Create input fields for existing username and password
        existing_username = st.text_input('Existing Username')
        existing_password = st.text_input('Existing Password', type='password')

        # Create a button to log in
        if st.button('Log In'):
            # Check if username and password fields are not empty
            if existing_username and existing_password:
                # Read existing user data from the text file
                with open('user_credentials.txt', 'r') as f:
                    user_data = f.read().split('\n')
                # Check if the username and password match any of the credentials in the text file
                for user in user_data:
                    if user:
                        username, password = user.split(',')
                        if existing_username == username and existing_password == password:
                            st.success('Successfully logged in.')
                            logged_in = True
                            # Clear input fields
                            existing_username = ""
                            existing_password = ""
                            break
                else:
                    st.error('Invalid username or password.')
            else:
                st.error('Please enter a username and password.')
    
    # Show the home page if user is logged in
    if logged_in:
        st.write('Welcome to the home page!')
        # You can add your own content here
