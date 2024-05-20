from cryptography import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    """
    The function `load_key` reads and returns the content of a file named "key.key" in binary mode.
    :return: The function `load_key()` is returning the contents of the "key.key" file as a binary
    string.
    """
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    """
    The function reads and decrypts passwords from a file and prints them along with the corresponding
    usernames.
    """
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    """
    The `add` function takes user input for an account name and password, encrypts the password, and
    appends the account name and encrypted password to a file.
    """
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# The `while True` loop in the provided Python code is creating an interactive menu for the user to
# either add a new password or view existing passwords. Here's how it works:
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
