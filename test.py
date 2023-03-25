import streamlit as st
import urllib.request
import csv

# Set the URL of the raw CSV file in your GitHub repository
csv_url = "https://github.com/PaulDHcad/mti820/blob/main/users.csv"

# Use urllib to read the contents of the CSV file from the URL
response = urllib.request.urlopen(csv_url)

# Use csv.reader to parse the contents of the CSV file
reader = csv.reader(response.read().decode('utf-8').splitlines())

# Iterate through the rows of the CSV file and display them in a Streamlit table
for row in reader:
    st.write(row)
