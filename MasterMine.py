"""'import random' is a Python statement that imports the 'random' module. This module provides functions for generating random numbers, choosing random elements, shuffling sequences, and more. In this code snippet, the 'random' module is used to generate a random code by selecting random colors from the 'COLORS' list.
"""
import random

""" The lines 'COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']', 'TRIES = 10', and 'CODE_LENGTH = 4' are defining constants in the Python code snippet.
"""
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    """
    The function 'generate_code' creates a list of random colors with a specified length.
    :return: A list of randomly generated colors with a length specified by the variable 'CODE_LENGTH'.
    """
    code = []
    """ The code snippet 'for _ in range(CODE_LENGTH): color = random.choice(COLORS) code.append(color)' is generating a random code by selecting colors from the 'COLORS' list. Here's a breakdown of what each part of this code snippet does: """
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


""" 'code = generate_code()' is calling the 'generate_code()' function to create a random code by selecting random colors from the 'COLORS' list. The generated code is then stored in the variable 'code' for later use in the game.
"""
code = generate_code()


def guess_code():
    """
    The function 'guess_code' prompts the user to enter a guess for a code, ensuring the guess is of the correct length and contains valid colors. :return: The function 'guess_code()' is returning the list of colors inputted by the user after validating the input.
    """

    """ This block of code is part of the 'guess_code()' function in the Python script. Here's a breakdown of what it does:
    """
    while True:
        guess = input("Enter your guess: ").upper().split(" ")

        """ The code snippet you provided is a part of the 'guess_code()' function in the Python script. """
        if len(guess) != CODE_LENGTH:
            print("Yuo must guess {CODE_LENGTH} colors.")
            continue

        """ This block of code is a loop that iterates over each color in the 'guess' list inputted by the user. It checks if each color is a valid color by verifying if it exists in the 'COLORS' list.
        """
        for color in guess:
            if color not in COLORS:
                print(f"{color} is not a valid color.")
                break
        else:
            break
    return guess


def check_code(guess, real_code):
    """
    The function 'check_code' compares a guess with a real code to determine the number of correct
    colors in correct positions and the number of correct colors in incorrect positions.
    :param guess: The 'guess' parameter represents the player's guess for a code in a game. It is a list of colors representing the player's attempt to guess the code :param real_code: The 'real_code' parameter in the 'check_code' function represents the actual secret code that the player is trying to guess. It is a list of colors or symbols that make up the code. The function compares this 'real_code' with the 'guess' provided by the player to determine the :return: The function 'check_code' returns a tuple containing the number of correct positions and the number of incorrect positions in the guess compared to the real code.
    """
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    """
    This block of code is part of the 'check_code' function in the Python script. Here's a breakdown of what it does:
    """
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    """
    This block of code is iterating over each pair of colors in the 'guess' list and the 'real_code' list simultaneously using the 'zip()' function.
    """
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[real_color] -= 1

    """
    This block of code is iterating over each pair of colors in the 'guess' list and the 'real_code' list simultaneously using the 'zip()' function. It checks if the 'guess_color' is in the 'color_counts' dictionary and if the count of that color is greater than 0. If these conditions are met, it increments the 'incorrect_pos' counter by 1 and decreases the count of that color in the 'color_counts' dictionary by 1 to keep track of the colors that have been used in the incorrect positions. This logic helps in determining the number of correct colors in incorrect positions when comparing the player's guess with the actual secret code.
    """
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    """
    This Python function is a game where the player has a limited number of tries to guess a secret code
    using a combination of colors.
    """
    print(f'Welcome to the MasterMine. you have {
          TRIES} to guess the code ... ')

    print(f'The Valid colors are:', *COLORS)

    code = generate_code()
    # print(code)

    """
    This part of the code snippet is the main game loop where the player has a limited number of tries ('TRIES') to guess the secret code. Here's a breakdown of what happens within thi loop:
    """
    for attemps in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f'You guessed in {attemps} tries.')
            break

        print(f'Correct Positions: {
              correct_pos} | Incorrect Positions: {incorrect_pos}')
    else:
        print('You ran out of tries, the code was:', *code)


if __name__ == "__main__":
    """
    The 'if __name__ == "__main__":' block in Python is a common idiom used to ensure that the code inside it is only executed if the script is run directly as the main program and not imported as a module into another script.
    """
    game()

# Good Luck
