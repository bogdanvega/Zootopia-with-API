import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetches the animals for the animal 'animal_name' from the API.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics':
        {
        ...
        }
    },
    """

    api_header = {
        'X-Api-Key': API_KEY
    }
    request_url = API_URL + f"{animal_name}"
    response = requests.get(request_url, headers=api_header)
    if response.status_code == requests.codes.ok:
        animals_data = response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"
    return animals_data

