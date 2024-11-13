from flask import Flask, render_template
import requests
import random
import os

app = Flask(__name__)

# Your Pixabay API Key
PIXABAY_API_KEY = '47047535-264964c8527d2d5233afb57f8'

def get_random_country():
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()
    country = random.choice(countries)
    return {
        "name": country.get("name", {}).get("common", "Unknown Country"),
        "description": f"{country.get('name', {}).get('common', 'Unknown Country')} is a country in {country.get('region', 'Unknown Region')}."
    }

def get_country_image(country_name):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={country_name}&image_type=photo&category=places"
    response = requests.get(url)
    data = response.json()
    if data.get("hits"):
        return data["hits"][0]["webformatURL"]
    return "https://via.placeholder.com/600x400?text=Image+Not+Available"

@app.route('/')
def index():
    country_data = get_random_country()
    image_url = get_country_image(country_data["name"])
    return render_template("index.html", country_data=country_data, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
