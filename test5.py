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
    st.write('Enter your credentials below to sign up or log in.')

    # Create input fields for username and password
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Create a button to sign up or log in
    if st.button('Sign Up'):
        # Check if username and password fields are not empty
        if username and password:
            # Read existing user data from the CSV file
            user_data = read_user_data()
            # Check if the username already exists in the CSV file
            usernames = [user[0] for user in user_data]
            if username in usernames:
                st.error('Username already exists. Please choose a different one.')
            else:
                # Write the new user credentials to the CSV file
                write_user_data(username, password)
                st.success('Successfully signed up. Please log in.')
        else:
            st.error('Please enter a username and password.')
    elif st.button('Log In'):
        # Check if username and password fields are not empty
        if username and password:
            # Read existing user data from the CSV file
            user_data = read_user_data()
            # Check if the username and password match any of the credentials in the CSV file
            for user in user_data:
                if username == user[0] and password == user[1]:
                    st.success('Successfully logged in.')
                    return
            st.error('Invalid username or password.')
        else:
            st.error('Please enter a username and password.')

if __name__ == '__main__':
    app()
