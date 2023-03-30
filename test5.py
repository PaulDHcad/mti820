import streamlit as st
import csv

# Create a function to read user credentials from the CSV file
def read_user_data():
    with open('user_credentials.csv', 'r') as f:
        reader = csv.reader(f)
        user_data = list(reader)
    return user_data

# Create a function to write user credentials to the CSV file
def write_user_data(username, password):
    with open('user_credentials.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

# Define the Streamlit app
def app():
    st.title('Sign-up/Login Page')

    # Define the layout for the sign-up and login forms
    col1, col2 = st.beta_columns([1, 1])

    with col1:
        st.write('Sign Up')
        # Create input fields for new username and password
        new_username = st.text_input('New Username')
        new_password = st.text_input('New Password', type='password')

        # Create a button to sign up
        if st.button('Sign Up'):
            # Check if username and password fields are not empty
            if new_username and new_password:
                # Read existing user data from the CSV file
                user_data = read_user_data()
                # Check if the username already exists in the CSV file
                usernames = [user[0] for user in user_data]
                if new_username in usernames:
                    st.error('Username already exists. Please choose a different one.')
                else:
                    # Write the new user credentials to the CSV file
                    write_user_data(new_username, new_password)
                    st.success('Successfully signed up. Please log in.')
            else:
                st.error('Please enter a username and password.')

    with col2:
        st.write('Log In')
        # Create input fields for existing username and password
        existing_username = st.text_input('Existing Username')
        existing_password = st.text_input('Existing Password', type='password')

        # Create a button to log in
        if st.button('Log In'):
            # Check if username and password fields are not empty
            if existing_username and existing_password:
                # Read existing user data from the CSV file
                user_data = read_user_data()
                # Check if the username and password match any of the credentials in the CSV file
                for user in user_data:
                    if existing_username == user[0] and existing_password == user[1]:
                        st.success('Successfully logged in.')
                        return
                st.error('Invalid username or password.')
            else:
                st.error('Please enter a username and password.')

    # Add a vertical line between the two columns
    st.markdown('<style> .st-ae {border-right: 1px solid #ddd;padding-right: 1rem;}</style>', unsafe_allow_html=True)

if __name__ == '__main__':
    app()
