import requests
import streamlit as st
#import main_app as st
import random

# Pixabay API setup
PIXABAY_API_KEY = '47047535-264964c8527d2d5233afb57f8'

# Function to get a random country data
def get_random_country():
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()
    country = random.choice(countries)
    name = country['name']['common']
    description = f"{name} is a country in {country['region']} with a population of {country['population']}."
    return {"name": name, "description": description}

# Function to get image from Pixabay API
def get_country_image(country_name):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={country_name}&image_type=photo"
    response = requests.get(url)
    data = response.json()
    if data['hits']:
        return data['hits'][0]['webformatURL']
    return "https://via.placeholder.com/600x400?text=Image+Not+Available"

# Streamlit layout
st.title("Daily Explorer")

# Fetch country data
country_data = get_random_country()
st.header(country_data['name'])
st.write(country_data['description'])

# F
