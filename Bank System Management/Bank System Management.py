import math
import os
"""
    The provided Python code includes functions for an online banking system allowing users to sign in,
    log in, perform banking operations, and calculate compound interest.
"""


def clear_screen():
    """
    The 'clear_screen' function in Python uses the 'os.system' method to clear the screen by executing
    the 'cls' command.
    """
    os.system('cls')


def signin():
    """
    The 'signin' function prompts the user to enter their name and a 6-digit pin, ensuring the pin is of
    the correct length before acknowledging the account creation.
    """
    global name
    global pin
    global Current_Balance  # Current Balance
    name = str(input('Please Enter your name: '))
    print('-' * 25)
    pin = str(input('Enter your 6 digit pin: '))
    print('-' * 25)
    if len(pin) == 6:
        pin = pin
    else:
        while len(pin) != 6:
            print('The pin must be 6 digits long!')
            pin = str(input('Enter your 6 digit pin: '))
            if len(pin) == 6:
                pin = pin
    print('Thanks for creating your bank account,', name)
    print('-' * 25)


def forgotpin():
    """
    The function 'forgotpin' allows the user to enter a new 6-digit pin and updates it if the input is
    valid.
    """
    recoverpin = str(input('Enter your new 6 digit pin: '))
    if len(recoverpin) != 6:
        print('The pin must be 6 digits long!')
        print('-' * 25)
        forgotpin()
    else:
        pin = recoverpin
        print('Your pin has been changed successfully!')
        print('-' * 25)
        login()


def depositinterest(p, r, t):
    """
    The function calculates the amount of money after earning compound interest for a given principal
    amount, interest rate, and time period.

    param p: The parameter 'p' represents the principal amount or initial deposit. It is the amount of
    money that is initially deposited or invested
    param r: The parameter 'r' in the 'depositinterest' function represents the interest rate. It is
    the rate at which interest is calculated on the principal amount 'p' over a given time period 't'
    param t: The parameter 't' in the 'depositinterest' function represents the time in years for which
    the interest is calculated
    return: The function 'depositinterest' calculates the amount of money after earning interest on a
    principal amount. It returns the final amount 'a' after applying the formula A = P * e^(rt), where P
    is the principal amount, r is the interest rate, t is the time period, and e is the base of the
    natural logarithm.
    """
    # A = Pe^(rt)
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    a = p * e
    return a


def login():
    """
    The 'login()' function in Python allows users to perform banking operations such as deposit,
    withdraw, transfer, check balance, and calculate compound interest after entering their name and
    pin.
    """
    name1 = str(input('Enter your name: '))
    pin1 = str(input('Enter your 6 digit pin: '))
    if name1 == name1 and pin1 == pin1:
        print('welcome back,', name)
        print('Please choose an option: ')
        listmenu = [
            '1-deposit\n2-withdraw\n3-transfer\n4-check balance\n5-deposit interest rate\n6-calculate compound interest']

        for b in listmenu:
            print(b)
            print('-' * 25)

        choose = int(input('Please enter your choice: '))
        print('-' * 25)

        d = 0  # represent deposit
        w = 0  # represent withdraw
        Current_Balance = 0  # represent current balance

        if choose == 1:  # deposit
            d = int(input('Enter the amount you want to deposit: '))
            Current_Balance = d
            print('your current balance is:', str(Current_Balance))

        elif choose == 2:  # withdraw

            w = int(input('Enter the amount you want to withdraw: '))
            if w > Current_Balance:
                print('You dont have enough money in your account')
                login()
            else:
                Current_Balance = d - w
                print(w + ' has been withdrawn from your account ',
                      'and your current balance is: ', Current_Balance)

        elif choose == 3:  # transfer
            dest = str(
                input('Enter the account number of your destination in 8 digits: '))
            if len(dest) == 8:
                amount = int(input('Enter the amount you want to transfer: '))
                if amount > Current_Balance:
                    print('You dont have enough money in your account')
                    login()
                else:
                    Current_Balance = d - amount
                    print(amount + ' has been transfered to account number: ',
                          dest, 'and your current balance is: ', Current_Balance)
                    print('your current balance is: ', Current_Balance)
            else:
                print(
                    'the transaction has been rejected since the destination account number is invalid')
                login()
        elif choose == 4:  # check balance
            print('your current balance is: ', Current_Balance)
        elif choose == 5:  # deposit interest rate
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
                print('your current interest rate is: ', rate, '%')

        elif choose == 6:  # calculate compound interest
            listoption = [
                '1-Calculate your deposit compound interest based on your Current_Balance,\n2-Calculate your deposit compound interest based on your interest rate']
            for a in listoption:
                print(a)
            choose = int(input('Please enter your choice: '))
            if choose == 1:
                timing = str(input('Enter the timing of your deposit: '))

                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print('your current balance rate is: ', ratex, '%')
                print(depositinterest(Current_Balance, ratex, timing))

            elif choose == 2:
                timing1 = str(input('Enter the timing of your deposit: '))
                money = str(input('Enter the amount you want to deposit: '))
                money = int(money)

                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print('your current balance rate is: ', ratex, '%')
                print(depositinterest(money, ratex, timing1))
        else:
            print('option is not available')
            login()
    else:
        print('Either of your name or pin is wrong, did you create your account?')
        list1 = ['1 for yes', '2 for no']
        for i in list1:
            print(i)
        inp = int(input('enter your choice below: '))
        if inp == 1:
            list2 = ['1-attemot to signin again', '2-forgotpin']
            for e in list2:
                print(e)

            theanswer = int(input('Please enter your choice: '))

            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print('option is not available')
                login()
        elif inp == 2:
            print('Please create your account first')
            signin()
    exit()


def mainmenu():
    """
    The 'mainmenu' function in Python presents a menu for users to either sign in or log in to an online
    banking system.
    """
    clear_screen()
    print('Welcome to the Online Banking System!')
    optionone = str(input('1-signin, 2-login: '))
    print('-' * 25)
    if optionone == "1":
        signin()
    elif optionone == "2":
        login()
    else:
        print('option is not available')
        mainmenu()
    print('-' * 25)
    exit()


def exit():
    """
    The 'exit()' function prompts the user to confirm if they want to exit, and either thanks them for
    using the services or redirects them to the main menu based on their response.
    """
    answer = str(input('Do you want to exit? '))
    if answer == 'yes':
        print('Thank you for using our services')
    elif answer == 'no':
        mainmenu()
    else:
        print('option is not available')
        exit()


# The 'mainmenu()' function in the provided Python code is presenting a menu for users to choose
# between signing in or logging in to an online banking system. It clears the screen, displays a
# welcome message for the online banking system, and prompts the user to input either '1' for signing
# in or '2' for logging in. Depending on the user's choice, it calls the 'signin()' function if '1' is
# selected or the 'login()' function if '2' is selected. If an invalid option is entered, it prompts
# the user that the option is not available and recursively calls 'mainmenu()' again.
if __name__ == '__main__':
    mainmenu()
