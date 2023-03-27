import streamlit as st
import csv
import urllib.request
import hashlib
import os
import random

# Set the URL of the raw CSV file in your GitHub repository
# csv_url = "https://github.com/PaulDHcad/mti820/blob/b009b2955a451ab67350ba72b89116c85348a845/users.csv"

# Use urllib to read the contents of the CSV file from the URL
# response = urllib.request.urlopen(csv_url)

# Use csv.reader to parse the contents of the CSV file
# USER_STORAGE_FILE = csv.reader(response.read().decode('utf-8').splitlines())

@st.cache
def generate_checkbox(checkbox_value):
    return checkbox_value

# Define the path to the user storage file
Countries = ["-- Sélectionner un pays parmi la liste --", "Afghanistan", "Afrique du Sud", "Albanie", "Algérie", "Allemagne", "Andorre", "Angola", "Antigua-et-Barbuda", "Arabie saoudite", "Argentine", "Arménie", "Australie", "Autriche", "Azerbaïdjan", "Bahamas", "Bahreïn", "Bangladesh", "Barbade", "Bélarus", "Belgique", "Belize", "Bénin", "Bhoutan", "Bolivie", "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie", "Burkina Faso", "Burundi", "Cambodge", "Cameroun", "Canada", "Cap-Vert", "Chili", "Chine", "Chypre", "Colombie", "Comores", "Congo, République démocratique du", "Congo, République du", "Corée du Nord", "Corée du Sud", "Costa Rica", "Côte d'Ivoire", "Croatie", "Cuba", "Danemark", "Djibouti", "Dominique", "République dominicaine", "Égypte", "Émirats arabes unis", "Équateur", "Érythrée", "Espagne", "Estonie", "États-Unis", "Éthiopie", "Fidji", "Finlande", "France", "Gabon", "Gambie", "Géorgie", "Ghana", "Grèce", "Grenade", "Guatemala", "Guinée", "Guinée équatoriale", "Guinée-Bissau", "Guyana", "Haïti", "Honduras", "Hongrie", "Inde", "Indonésie", "Irak", "Iran", "Irlande", "Islande", "Israël", "Italie", "Jamaïque", "Japon", "Jordanie", "Kazakhstan", "Kenya", "Kirghizistan", "Kiribati", "Koweït", "Laos", "Lesotho", "Lettonie", "Liban", "Liberia", "Libye", "Liechtenstein", "Lituanie", "Luxembourg", "Macédoine du Nord", "Madagascar", "Malaisie", "Malawi", "Maldives", "Mali", "Malte", "Maroc", "Îles Marshall", "Maurice", "Mauritanie", "Mexique", "Micronésie", "Moldavie", "Monaco", "Mongolie", "Monténégro", "Mozambique", "Myanmar", "Namibie", "Nauru", "Népal", "Nicaragua", "Niger", "Nigeria", "Niue", "Norvège", "Nouvelle-Zélande", "Oman", "Ouganda", "Ouzbékistan", "Pakistan", "Palaos", "Panama", "Papouasie-Nouvelle-Guinée", "Paraguay", "Pays-Bas", "Pérou", "Philippines", "Pologne", "Portugal", "Qatar", "Roumanie", "Royaume-Uni", "Russie", "Rwanda", "Saint-Christophe-et-Niévès", "Saint-Marin", "Saint-Vincent-et-les-Grenadines", "Sainte-Lucie", "Salomon, Îles", "Salvador", "Samoa", "Sao Tomé-et-Principe", "Sénégal", "Serbie", "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Somalie", "Soudan", "Soudan du Sud", "Sri Lanka", "Suède", "Suisse", "Suriname", "Swaziland", "Syrie", "Tadjikistan", "Tanzanie", "Tchad", "République tchèque", "Thaïlande", "Timor-Leste", "Togo", "Tonga", "Trinité-et-Tobago", "Tunisie", "Turkménistan", "Turquie", "Tuvalu", "Ukraine", "Uruguay", "Vanuatu", "Vatican, cité du", "Venezuela", "Viêt Nam", "Yémen", "Zambie", "Zimbabwe"]
Genres = ["Animation/Animé","Aventure","Romantique","Comédie","Action","Familial","Dramatique","Crimes","Fantaisie","Science fiction","Thriller","Musical","Horreur","Documentaire","Mystère","Western","Guerre","Film de télévision"]
USER_STORAGE_FILE = 'users.csv'

# If the user storage file doesn't exist, create an empty file
if not os.path.isfile(USER_STORAGE_FILE):
    with open(USER_STORAGE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "surname", "username", "location", "password", "email", "idfavoritegenre", "birthyear"])

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
            break
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

def main():
    
    # Add a title
    st.title("Se connecter ou s'inscrire")

    # Add radio buttons to select login or sign up
    choice = st.radio("Sélectionner :", ("Se connecter", "S'inscrire"))

    # If the user selects sign up
    if choice == "S'inscrire":
        # Add user input fields for username, password, and email
        input_name = st.text_input("Prénom", value="")
        input_surname = st.text_input("Nom", value="")
        input_username = st.text_input("Nouveau nom d'utilisateur", value="")
        input_password = st.text_input("Nouveau mot de passe", value="", type="password")
        input_email = st.text_input("Adresse courriel", value="")
        input_location = st.selectbox("Select a country", Countries)
        input_birthyear = st.number_input("Année de naissance", value=2000, step=1)

        # Add a button to submit the sign up information
        if st.button("S'inscrire"):
            if input_name=="":
                st.error('Le champ Prénom est vide.')

            else:
                if input_surname=="":
                    st.error('Le champ Nom est vide.')

                else:
                    if input_username=="":
                        st.error("Le champ Nom d'utilisateur est vide.")

                    else:
                        if input_password=="":
                            st.error('Le champ Mot de passe est vide.')

                        else:
                            if input_email=="":
                                st.error('Le champ Adresse courriel est vide.')

                            else:
                                if input_location=="-- Sélectionner un pays parmi la liste --":
                                    st.error('Veuillez choisir un pays parmi la liste dans le champ Pays')

                                else:
                                    if input_birthyear=="" or input_birthyear < 1900 or input_birthyear > 2023:
                                        st.error('Veuillez entrer une année correcte dans le champ Année de naissance')

                                    else:
                                        if username_exists(input_username):
                                            st.error("Nom d'utilisateur déjà utilisé. Veuillez en choisir un autre.")

                                        else:
                                            if email_exists(input_email):
                                                st.error("Cette adresse courriel est déjà associée à un compte.")
                                            else: 
                                                add_user(input_name, input_surname, input_username, input_password, input_email, input_location, input_birthyear)
                                                st.success("Inscription effectuée avec succès.")
                                                #st.experimental_rerun()

    # If the user selects login
    elif choice == "Se connecter":
        # Add user input fields for username and password
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")

        # Add a button to submit the login credentials
        if st.button("Se connecter"):
            if check_credentials(username, password):

                st.success("Connecté en temps que {}".format(username))
                selected_genre = []

                # Add the rest of your application logic here
                userdata = get_user_details(username)
                st.title("Vos informations")
                st.write("Votre ID :", userdata[0])
                st.write("Votre prénom :", userdata[1])
                st.write("Votre nom :", userdata[2])
                st.write("Votre nom d'utilisateur :", userdata[3])
                st.write("Votre adresse courriel :", userdata[6])
                st.write("Votre localisation :", userdata[4])
                st.write("Votre année de naissance :", userdata[8])

                # Option of favorites genres
                st.title("Favourites genres :")
                st.write("Vos genre favoris:", userdata[7])
                col1, col2 = st.columns(2)
                with col1:
                    selected = st.checkbox(Genres[0])
                    if selected:
                        selected_genre.append(Genres[0])

                    selected = st.checkbox(Genres[1])
                    if selected:
                        selected_genre.append(Genres[1])

                    selected = st.checkbox(Genres[2])
                    if selected:
                        selected_genre.append(Genres[2])

                    selected = st.checkbox(Genres[3])
                    if selected:
                        selected_genre.append(Genres[3])                  

                    selected = st.checkbox(Genres[4])
                    if selected:
                        selected_genre.append(Genres[4])                   

                    selected = st.checkbox(Genres[5])
                    if selected:
                        selected_genre.append(Genres[5])     

                    selected = st.checkbox(Genres[6])
                    if selected:
                        selected_genre.append(Genres[6])                    

                    selected = st.checkbox(Genres[7])
                    if selected:
                        selected_genre.append(Genres[7])

                with col2:
                    selected = st.checkbox(Genres[8])
                    if selected:
                        selected_genre.append(Genres[8])

                    selected = st.checkbox(Genres[9])
                    if selected:
                        selected_genre.append(Genres[9])

                    selected = st.checkbox(Genres[10])
                    if selected:
                        selected_genre.append(Genres[10])

                    selected = st.checkbox(Genres[11])
                    if selected:
                        selected_genre.append(Genres[11])                  

                    selected = st.checkbox(Genres[12])
                    if selected:
                        selected_genre.append(Genres[12])                   

                    selected = st.checkbox(Genres[13])
                    if selected:
                        selected_genre.append(Genres[13])     

                    selected = st.checkbox(Genres[14])
                    if selected:
                        selected_genre.append(Genres[14])                    

                    selected = st.checkbox(Genres[15])
                    if selected:
                        selected_genre.append(Genres[15])                   

                if st.button("Valider la saisie"):
                    writer.writerow([_, _, _, _, _, _, _, selected_genre, _])

            else:
                st.error("Nom d'utilisateur et/ou mot de passe incorrect(s).")
                
if __name__ == '__main__':
    main()
