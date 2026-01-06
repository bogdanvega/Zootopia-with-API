from animal_data_handle import replace_animals_info

def main():
    """ Main function that calls the function that generates the html file."""
    animal = input("Enter a name of an animal: ")
    replace_animals_info(animal)


if __name__ == "__main__":
    main()
