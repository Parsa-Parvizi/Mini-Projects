import random
from dictionary import my_dict
import os


def Clean_Screen():
    os.system('cls')


def generate_question():
    """
    This Python function generates a multiple-choice question about countries and their capitals.
    :return: A tuple containing the country, its capital, and a list of options for a multiple-choice
    question.
    """
    country, capital = random.choice(list(my_dict.items()))
    options = list(my_dict.values())
    options.remove(capital)
    options = random.sample(options, 3)
    options.append(capital)
    random.shuffle(options)
    awnsers = country, capital, options
    return awnsers


def quiz_mode():
    """
    This function implements a quiz mode where the user is asked 5 questions about country capitals and
    receives a score based on their answers.
    """
    score = 0
    next_oppertunity = 0
    for _ in range(5):  # Ask 5 questions
        country, capital, options = generate_question()
        print(f"What is the capital of {country}?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Enter the number of your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        try:
            if options[answer - 1] == capital:
                print("Correct!")
                score += 1
            elif answer == 0:
                next_oppertunity += 1
                print(f'you jusr pressed next.')
                continue
            else:
                print(f"Sorry, the correct answer is {capital}.")
            if next_oppertunity == 3:
                print(f'Game Over')
                break
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 4.")
    print(f"Your final score is {score} out of 5.")
    if score == 5:
        print('*' * 20, 'You are Awesome', '*' * 20)
    elif score == 4:
        print('*' * 20, 'You are Good', '*' * 20)
    elif score == 3:
        print('*' * 20, 'You are Average', '*' * 20)
    elif score == 2:
        print('*' * 20, 'You are Beginner', '*' * 20)
    elif score == 1:
        print('*' * 20, 'You are Beginner', '*' * 20)
    elif score == 0:
        print('*' * 20, 'You are Bad', '*' * 20)
    play_agian()


def guess_mode():
    """
    The function `guess_mode` allows the user to guess the capital of a randomly selected country from a
    dictionary and provides feedback based on the number of attempts made.
    """
    counter = 0
    time_played = 0
    items = my_dict.items()
    global random_items
    random_items = random.choice(list(items))
    print(f'Country is: {random_items[0]}')

    while True:
        user = input('guess the capital of the this Country? ').title()
        if user == 'Next':

            print('You just skip your question.')
            print(f'you can skip')
            guess_mode()

        elif user == random_items[1]:
            print('correct, End of the Game')
            time_played += 1
            break

        elif user != random_items[1]:
            counter += 1
            print(f'Wrong, You have {5 - counter} attempts left')
            if counter == 5:
                print('Game Over')
                break

    if time_played == 5:
        print('*' * 20, 'You are Awesome', '*' * 20)
    elif time_played == 4:
        print('*' * 20, 'You are Good', '*' * 20)
    elif time_played == 3:
        print('*' * 20, 'You are Average''*' * 20)
    elif time_played == 2:
        print('*' * 20, 'You are Beginner', '*' * 20)
    elif time_played == 1:
        print('*' * 20, 'You are Beginner', '*' * 20)
    elif time_played == 0:
        print('*' * 20, 'You are Bad', '*' * 20)
    play_agian()


def play_agian():
    """
    The function `play_again()` prompts the user to choose whether to play the quiz again or not, and
    based on the input, either restarts the quiz or ends the program.
    """
    another_input = int(
        input('Do you wanna play again?\n1. Yes\n2. No\nYour input: '))
    if another_input == 1:
        print('*' * 20, 'Her we Go Again', '*' * 20)
        quiz_mode()
    elif another_input == 2:
        print('See you Later')
    else:
        print('Invalid Input')
        play_agian()


def main():
    """
    The main function presents a menu for the user to choose between quiz mode, guess mode, or exiting
    the program, handling the user's input accordingly.
    """
    print('*' * 10, 'Welcome to The guess or Pick correct Capital of world Country', '*' * 10)
    main_input = int(
        input('Which mode do you want to play?\n1. Quiz Mode\n2. Guess Mode\n3. Exit\nyour input: '))
    if main_input == 1:
        quiz_mode()
    elif main_input == 2:
        guess_mode()
    elif main_input == 3:
        print('See you Later')
    else:
        print('Invalid Input')
        main()


if __name__ == '__main__':
    Clean_Screen()
    main()
