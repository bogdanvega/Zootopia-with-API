from data_fetcher import fetch_data
from html_file_handle import load_html_data, create_html_file

def get_animal_name():
    """ Gets the name of the animal from the user. """
    return input("Enter a name of an animal: ")


def format_animals_html():
    """
    Gets the data from the API of the wanted animal,
    then calls the function that adds information of every
    type animal into a string formatted like html.
    Returns this string.
    """
    output = ''
    animal = get_animal_name()
    data = fetch_data(animal)
    if not data:
        output += f"""<h2>The animal "{animal}" doesn't exist.</h2>"""
    # treating the case when a different status
    # than ok is returned from the API request
    elif type(data) is str:
        output += f"""<h2>{data}</h2>"""
    else:
        for animal in data:
            output += serialize_animal(animal)
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


def generate_website():
    """
    Loads the html template and animals information into string data.
    Replaces the template text from the "animals_template.html" with
    animals information.
    Then calls the function to generate the new html file with animals information.
    """
    html_template = load_html_data('animals_template.html')
    animals_information = format_animals_html()
    new_html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_information)
    create_html_file(new_html_content)
    print("Website was successfully generated to the file animals.html.")
