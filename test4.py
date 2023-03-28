import streamlit as st
import pandas as pd
import hashlib

def hash_password(password):
    salt = hashlib.sha256(str.encode(password)).hexdigest()[:8]
    hashed_password = hashlib.sha256(str.encode(password+salt)).hexdigest()+":"+salt
    return hashed_password
  
import random
def generate_id():
    return random.randint(100000, 999999)

def read_csv_file(filename):
    df = pd.read_csv(filename)
    return df
  
def write_csv_file(data, filename):
    df = pd.read_csv(filename)
    df = df.append(data, ignore_index=True)
    df.to_csv(filename, index=False)
    
def sign_in():
    st.header("Sign In")
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    location = st.selectbox("Country", ["Country 1", "Country 2", "Country 3"])
    birthyear = st.slider("Birthyear", 1900, 2023, 2000)
    fav_genres = st.multiselect("Favorite Movie Genres", ["Action", "Comedy", "Drama", "Horror", "Romance"])
    if st.button("Sign In"):
        hashed_password = hash_password(password)
        user_id = generate_id()
        data = {"ID": user_id, "Name": name, "Surname": surname, "Username": username, "Password": hashed_password, "Email": email, "Location": location, "Birthyear": birthyear, "Favorite Genres": fav_genres}
        write_csv_file(data, "user_data.csv")
        st.success("You have successfully signed in!")

def log_in():
    st.header("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        df = read_csv_file("user_data.csv")
        user_data = df.loc[df["Username"] == username]
        if user_data.empty:
            st.warning("Username not found.")
        else:
            hashed_password = user_data.iloc[0]["Password"]
            salt = hashed_password.split(":")[1]
            if hashed_password == hashlib.sha256(str.encode(password+salt)).hexdigest()+":"+salt:
                st.success("Logged in successfully!")
                user_id = user_data.iloc[0]["ID"]
                name = user_data.iloc[0]["Name"]
                surname = user_data.iloc[0]["Surname"]
                email = user_data.iloc[0]["Email"]
                location = user_data.iloc[0]["Location"]
                birthyear = user_data
                
                
