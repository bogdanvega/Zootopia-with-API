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
    try:
        animals_data = load_json_data('animals_data.json')
        for animal in animals_data:
            animal_name = animal.get("name", "")
            animal_diet = animal["characteristics"].get("diet", "")
            animal_location = animal.get("locations", "")
            animal_type = animal["characteristics"].get("type", "")

            if animal_name != "":
                print(f"Name: {animal_name}")
            if animal_diet != "":
                print(f"Diet: {animal_diet}")
            if animal_location != "":
                print("Location: ", end="")
                print(', '.join(map(str, animal_location)))
            if animal_type != "":
                print(f"Type: {animal_type}")
            print()
    except FileNotFoundError:
        print("File not found!")
