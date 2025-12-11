import json

def load_json_data(json_file_path):
    """ Loads a JSON file """
    with open(json_file_path, "r") as handle:
        return json.load(handle)


def load_html_data(html_file_path):
    """ Loads a html file """
    with open(html_file_path, "r") as file_object:
        return file_object.read()


def print_data():
    """
    Reads the content of a json file, then prints the name, diet,
    location and type of every animal.
    If one of these fields doesn’t exist, it doesn’t print it.
    """
    output = ""
    try:
        animals_data = load_json_data('animals_data.json')
        for animal in animals_data:
            animal_name = animal.get("name", "")
            animal_diet = animal["characteristics"].get("diet", "")
            animal_location = animal.get("locations", "")
            animal_type = animal["characteristics"].get("type", "")

            if animal_name != "":
                output += f"Name: {animal_name}\n"
            if animal_diet != "":
                output += f"Diet: {animal_diet}\n"
            if animal_location != "":
                output += "Location: "
                output += ', '.join(map(str, animal_location)) + "\n"
            if animal_type != "":
                output += f"Type: {animal_type}\n"
            output += "\n"
    except FileNotFoundError:
        output += "File not found!"

    print(output)

