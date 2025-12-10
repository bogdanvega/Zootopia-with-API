import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_data():
    """
    Reads the content of a json file, then prints the name, diet,
    location and type of every animal.
    If one of these fields doesn’t exist, it doesn’t print it.
    """
    animals_data = load_data('animals_data.json')
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

print_data()