import streamlit as st
import csv
import hashlib
import os
import random

# Define the path to the user storage file
USER_STORAGE_FILE = 'users.csv'
# If the user storage file doesn't exist, create an empty file
if not os.path.isfile(USER_STORAGE_FILE):
    with open(USER_STORAGE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "surname", "username", "location", "password", "email", "idfavoritegenre", "birthyear])

# Define a function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define a function to check if an ID number already exists in the CSV file
def id_number_exists(id_number):
    with open(USER_STORAGE_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == str(id_number):
                return True
    return False
                         
# Generate a random ID number that is not already in the CSV file
def new_id() :
    while True:
        id_number = random.randint(100000, 999999)
        if not id_number_exists(id_number):
    return id_number
                         
# Define a function to check if a username exists in the user storage file
def username_exists(username):
    with open(USER_STORAGE_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if username == row[3]:
                return True
    return False

# Define a function to check if a email is already used in the user storage file
def email_exists(email):
    with open(USER_STORAGE_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[6] == str(email):
                return True
    return False

# Define a function to add a new user to the user storage file
def add_user(name, surname, username, password, email, location, birthyear,):
    with open(USER_STORAGE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([new_id(), name, surname, username, location, hash_password(password), email, "", birthyear])

# Define a function to check if the login credentials are correct
def check_credentials(username, password):
    with open(USER_STORAGE_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if username == row[3] and hash_password(password) == row[5]:
                return True
    return False

# Define a function to get the user's details
def get_user_details(username):
    with open(USER_STORAGE_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if username == row[3]:
                return row
    return None

# Add a title
st.title("Se connecter ou s'inscrire")

# Add radio buttons to select login or sign up
choice = st.radio("Sélectionner :", ("Se connecter", "S'inscrire"))

# If the user selects sign up
if choice == "S'inscrire":
    # Add user input fields for username, password, and email
    new_username = st.text_input("Nom d'utilisateur")
    new_password = st.text_input("Mot de passe", type="password")
    new_email = st.text_input("Adresse courriel")
    new_location = st.text_input("Pays")

    # Add a button to submit the sign up information
    if st.button("S'inscrire"):
        if username_exists(new_username):
            st.error("Nom d'utilisateur déjà utilisé. Veuillez en choisir un autre.")

        else:
            if email_exists(new_email):
                st.error("Cette adresse courriel est déjà associée à un compte.")
            else: 
                add_user(new_username, new_password, new_email, new_location)
                st.success("Inscription effectuée avec succès.")

# If the user selects login
elif choice == "Se connecter":
    # Add user input fields for username and password
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    # Add a button to submit the login credentials
    if st.button("Se connecter"):
        if check_credentials(username, password):
            st.success("Connecté en temps que {}".format(username))
            # Add the rest of your application logic here
            userdata = retreive_userdata(username)
            st.title("Vos informations")
            st.write("Votre nom d'utilisateur :", userdata[0])
            st.write("Votre adresse courriel :", userdata[1])
            st.write("Votre localisation :", userdata[2])
        else:
            st.error("Nom d'utilisateur et/ou mot de passe incorrect(s).")
