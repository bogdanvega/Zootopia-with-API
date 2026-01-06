from html_file_handle import load_html_data, create_html_file
import requests

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "z0zx/8ToU4CZ5enIYNnxrw==cUQXkp4JQbKza6Wi"

def get_animal_info():
    """
    Fetches the fox data from the API, then calls the function that
    adds the name, diet, location and type of every fox type animal into a string
    formatted like html. Returns this string.
    """

    output = ''
    request_url = API_URL + "Fox"
    response = requests.get(request_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        animals_data = response.json()
        for animal in animals_data:
            output += serialize_animal(animal)
    else:
        print("Error:", response.status_code, response.text)

    return output


def serialize_animal(animal_data):
    """
    Adds for every animal the name, diet, location and type
    to an already formatted string for html parsing.
    If one of these fields doesn’t exist, it doesn’t add it.
    Returns the string.
    """
    animal_output = ''
    animal_name = animal_data.get('name', '')
    animal_diet = animal_data['characteristics'].get('diet', '')
    animal_location = animal_data.get('locations', '')
    animal_type = animal_data['characteristics'].get('type', '')

    if animal_name != '':
        animal_output += '<li class="cards__item">'
        animal_output += (f'<div class="card__title">{animal_name}</div>'
                   f'<p class="card__text">\n')
    if animal_diet != '':
        animal_output += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    if animal_location != '':
        animal_output += '<strong>Location:</strong> '
        animal_output += ', '.join(map(str, animal_location)) + '<br/>\n'
    if animal_type != '':
        animal_output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    animal_output += '</p></li>\n'
    return animal_output


def replace_animals_info():
    """
    Loads the html template and animals information into string data.
    Replaces the template text from the "animals_template.html" with
    animals information.
    Then calls the function to generate the new html file with animals information.
    """
    html_template = load_html_data('animals_template.html')
    animals_information = get_animal_info()
    if animals_information is None:
        print('File not found!')
    else:
        new_html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_information)
        create_html_file(new_html_content)
        print("animals.html successfully created!")
