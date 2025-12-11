import json

def load_json_data(json_file_path):
    """ Loads a JSON file """
    with open(json_file_path, 'r') as handle:
        return json.load(handle)