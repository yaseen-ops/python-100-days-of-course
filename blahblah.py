import json

FILE = "C:/Users/yaseen/secrets/secrets.json"


def get_secrets_from_text_file(file):
    """
    Function to get secrets from specific text file for specific operation
    It is having only one parameter as 'file' where have to provide the file name with absolute path
    """
    data_dict = {}
    with open(file) as file:
        for line in file:
            key, value = line.strip().split(" : ")
            data_dict[key] = value.strip()
    return data_dict


def get_secrets(json_file=FILE):
    """
    Function to retrieve secrets from JSON file
    By fault the JSON file path is set, it can be updated manually during fuction call
    """
    with open(json_file, "r") as file:
        data = json.load(file)
        return data
