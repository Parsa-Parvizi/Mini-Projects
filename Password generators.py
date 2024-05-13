# The lines 'import random', 'import string', and 'import os' are importing modules in Python.
import random
import string
import os


# The 'settings' dictionary is defining the default settings for the password generator program. Each
# key in the dictionary represents a setting option, and the corresponding value indicates whether
# that option is enabled ('True') or disabled ('False'). Here's what each setting option means:
settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 6
}


# The lines 'PASSWORD_MIN_LENGTH = 4' and 'PASSWORD_MAX_LENGTH = 30' are defining constants in the
# Python script.
PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30


def clear_screen():
    """
    The 'clear_screen' function in Python uses the 'os.system' method to clear the screen by executing
    the 'cls' command.
    """
    os.system('cls')


def get_user_password_length(option, default, pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):
    """
    This function prompts the user to enter a password length within a specified range or use a default
    value.

    :param option: The 'option' parameter is not being used in the 'get_user_password_length' function.
    It seems like it was defined as a parameter but not utilized within the function. If you intended to
    use it for some specific functionality, you may need to update the function accordingly
    :param default: The 'default' parameter in the 'get_user_password_length' function is the default
    password length that will be used if the user does not provide any input
    :param pw_min_length: The 'pw_min_length' parameter in the 'get_user_password_length' function
    represents the minimum allowed length for a password. This value is used to validate the user input
    for the password length. In the provided code snippet, the 'pw_min_length' is referenced in the
    error message that specifies the
    :param pw_max_length: The 'pw_max_length' parameter in the 'get_user_password_length' function
    represents the maximum allowed length for a password. This value is used to validate the user input
    for the password length. In the provided code snippet, the 'pw_max_length' is used in the validation
    check to ensure that
    :return: The function 'get_user_password_length' returns the user's chosen password length if it is
    within the specified range (4 to 30 characters), or the default password length if the user enters
    an empty string or an invalid input.
    """
    while True:
        user_input = input(f'Enter password length. Default is {
                           default}. enter: default: ')

        if user_input == '':
            return default

        if user_input.isdigit():
            user_password_length = int(user_input)
            if 4 <= user_password_length <= 30:
                return int(user_input)
            print('Invalid Input.')
            print(f'Password length should be between {
                  pw_min_length} and {pw_max_length}.')
        else:
            print('Invalid input, you should enter a number.')


def get_yes_or_no_for_setting(option, default):
    """
    The function 'get_yes_or_no_for_setting' prompts the user to include an option or not based on a
    default value and returns a boolean indicating the user's choice.

    :param option: The 'option' parameter in the 'get_yes_or_no_for_setting' function represents the
    setting or option for which the user is being asked to provide input (e.g., "Include notifications",
    "Enable dark mode", etc.)
    :param default: The 'default' parameter in the 'get_yes_or_no_for_setting' function represents the
    default value for the setting option. It is the value that will be returned if the user simply
    presses Enter without providing a specific input
    :return: The function 'get_yes_or_no_for_setting' returns a boolean value based on the user input.
    It returns 'True' if the user input is 'y' (indicating yes) and 'False' if the user input is 'n'
    (indicating no). If the user simply presses Enter without providing any input, it returns the
    default boolean value specified for the option.
    """
    while True:
        user_input = input(f'Include {option}? Default is {
                           default}. y: yes, n: no, enter: default:y so: ')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input, please try again.')


def get_setting_from_user(settings):
    """
    The function iterates through settings, prompting the user for input based on the setting type.

    :param settings: The 'settings' parameter is a dictionary containing various configuration options
    for a password generator. The keys in the dictionary represent different settings, and the values
    are the default values for those settings. The function 'get_setting_from_user' iterates over the
    settings and prompts the user to provide input for each setting
    """
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_setting(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def ask_if_change_setting(settings):
    """
    This Python function prompts the user to change default settings based on their input.

    :param settings: The 'settings' parameter in the 'ask_if_change_setting' function is likely a
    dictionary or some other data structure that holds the default settings for a particular application
    or system. The function prompts the user to see if they want to change the default settings and then
    calls another function 'get_setting_from_user
    """
    while True:
        user_answer = input(
            "Do you want change default setting ('y' for yes, 'n' for no)? ")

        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('-' * 5, 'Change Settings', '-' * 5, sep='')
                get_setting_from_user(settings)
            break
        else:
            print('Invalid.')


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)


def get_random_number():
    return random.choice('0123456789')


def get_random_symbol():
    return random.choice("""!@#$%^&*()<>?:{|}[]""")


def generate_random_char(choices):
    """
    The function 'generate_random_char' returns a random character based on the specified choices of
    uppercase letters, lowercase letters, symbols, numbers, or a space.

    :param choices: It seems like the 'choices' parameter in the 'generate_random_char' function is
    expected to be a list of strings representing different character types such as 'upper', 'lower',
    'symbol', 'number', or an empty string. Each string in the list corresponds to a specific type of
    character that
    :return: The function 'generate_random_char' returns a randomly selected character based on the
    input choices. It can return an uppercase letter, a lowercase letter, a symbol, a number, or a space
    character.
    """
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == '':
        return ' '


def password_generator(settings):
    """
    The function 'password_generator' generates a random password based on the specified settings.

    :param settings: It seems like you haven't provided the details of the 'settings' parameter. Could
    you please provide the details or let me know how I can assist you further with the
    'password_generator' function?
    :return: The function 'password_generator' returns a randomly generated password based on the
    settings provided. The password length is determined by the 'length' key in the settings dictionary.
    The characters used in the password are based on the settings for 'lower', 'upper', 'symbol',
    'number', and 'space' keys in the settings dictionary. The function generates a random character
    based on the selected choices for each
    """
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], [
                   'lower', 'upper', 'symbol', 'number', 'space']))
    # print(choices)

    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def ask_user_to_generate_another_password():
    """
    The function 'ask_user_to_generate_another_password' prompts the user to decide whether to
    regenerate a password or not.
    :return: The function 'ask_user_to_generate_another_password()' returns a boolean value. It returns
    'False' if the user enters 'n' to indicate they do not want to regenerate the password, and it
    returns 'True' if the user enters 'y' or presses Enter (empty input) to indicate they want to
    regenerate the password.
    """
    while True:
        user_answer = input('regenerate? (y: yes, n: no): ')

        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid')


def password_generator_loop(settings):
    """
    The function 'password_generator_loop' continuously generates passwords based on the provided
    settings until the user chooses to stop.

    :param settings: It seems like you have provided a snippet of code for a password generator function
    that includes a loop to continuously generate passwords until the user decides to stop. However, the
    details of the 'settings' parameter are missing in your message. If you can provide the specific
    settings or requirements for the password generation process
    """
    while True:
        print("-" * 20)
        print(f"Generated Password is: {password_generator(settings)}")

        if ask_user_to_generate_another_password() == False:
            break


def run():
    """
    The 'run' function clears the screen, asks the user if they want to change settings, generates a
    password based on the settings, and then prints a thank you message.
    """
    clear_screen()
    ask_if_change_setting(settings)
    print(f'your setting is: {settings}')
    password_generator_loop(settings)
    print('Thank you for choosing us.')


if __name__ == "__main__":
    run()
