import sys
import clipboard
import json

# The line `SAVED_DATA = "clipboard.json"` is assigning the string "clipboard.json" to the variable
# `SAVED_DATA`. This variable is used to store the file path where the clipboard data will be saved
# and loaded from. In this case, the clipboard data is being saved and loaded to/from a file named
# "clipboard.json".
SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    """
    The function `save_data` saves the provided data to a file specified by the filepath in JSON format.

    :param filepath: The `filepath` parameter is a string that represents the file path where the data
    will be saved. It should include the file name and extension (e.g., "data.json")
    :param data: Data is the information that you want to save to a file. It could be a dictionary,
    list, string, or any other type of data that you want to store in a file
    """
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    """
    The function `load_data` reads and returns data from a JSON file, or an empty dictionary if an error
    occurs.

    :param filepath: The `filepath` parameter in the `load_data` function is a string that represents
    the path to the file from which data needs to be loaded
    :return: An empty dictionary {} is being returned if an exception occurs during the loading of data
    from the specified file.
    """
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


# This block of code is checking the number of command-line arguments passed to the script. If exactly
# two arguments are provided, it proceeds to execute different actions based on the command provided.
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
