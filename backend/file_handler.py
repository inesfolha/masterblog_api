import json


def load_file(file_path):
    """ Loads a JSON file """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data

    except Exception as e:
        print(f'Error message: {str(e)}')


def save_file(filename, data_to_save):
    """Creates a new json file with the given file name and writes the provided content to it."""
    try:
        with open(filename, 'w') as f:
            json.dump(data_to_save, f)
            return filename

    except Exception as e:
        print(f'Error message: {str(e)}')
