import streamlit as st
import pandas as pd
import hashlib

# Load the user credentials from a CSV file
df_users = pd.read_csv("user_credentials.csv")

# Define a function to generate a unique ID for each user
def generate_user_id():
    return df_users["ID"].max() + 1 if len(df_users) > 0 else 1

# Define a function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define the sign-up page
def signup():
    st.title("Sign Up")
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    country = st.selectbox("Country", sorted(pd.read_csv("countries.csv")["name"]))
    birthyear = st.slider("Birth Year", 1900, 2023)
    genres = st.multiselect("Favorite Movie Genres", ["Action", "Comedy", "Drama", "Horror", "Romance"])
    if st.button("Sign Up"):
        hashed_password = hash_password(password)
        user_id = generate_user_id()
        df_users.loc[len(df_users)] = [user_id, name, surname, username, hashed_password, email, country, birthyear, genres]
        df_users.to_csv("user_credentials.csv", index=False)
        st.success("You have successfully signed up! Please log in.")

# Define the login page
def login():
    st.title("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        hashed_password = hash_password(password)
        user = df_users[(df_users["Username"] == username) & (df_users["Password"] == hashed_password)]
        if len(user) == 1:
            st.success("You have successfully logged in!")
            st.write(user.iloc[0])
            st.write("Favorite movie genres:", user["Favorite Movie Genres"].iloc[0])
        else:
            st.error("Incorrect username or password. Please try again.")

# Define the home page
def home(user):
    st.title("Home")
    st.write(user)
    st.write("Favorite movie genres:", user["Favorite Movie Genres"])

# Define the app
def app():
    st.set_page_config(page_title="Movie Genres App", page_icon=":movie_camera:")
    st.sidebar.title("Navigation")
    pages = {
        "Sign Up": signup,
        "Log In": login,
    }
    page = st.sidebar.radio("Go to", tuple(pages.keys()))
    user = None
    if page == "Sign Up":
        pages[page]()
    elif page == "Log In":
        username = st.session_state.get("username")
        if username:
            user = df_users[df_users["Username"] == username]
            home(user.iloc[0])
        else:
            login()
            if st.session_state.username:
                user = df_users[df_users["Username"] == st.session_state.username]
                home(user.iloc[0])

if __name__ == "__main__":
    app()
