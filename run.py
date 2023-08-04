"""
Modules
"""
import random
from random import randint
import sys
import time
import gspread
from google.oauth2.service_account import Credentials

choice = ["R", "P", "S"]
computer = choice[randint(0,2)]


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')

userscore = SHEET.worksheet('userinfo')

# data = sales.get_all_values()

# print(data)




def intro():
    """
    This is the opening to the game
    User can pick to play or read the instructions.
    """
    clear()
    print('')
    print_slow("Welcome to Rock Paper Scissors \n")
    print('')
    print_slow("     🪨  Vs 📄  Vs ✂️\n")
    print('')
    username = input("Please enter username: ")
    userscore.update_cell(3,1, username)
    sales_worksheet = SHEET.worksheet("userinfo")
    clear() 
    print("\nWould you like to read the Game Instructions " + username)
    answer = input("\nEnter Y to read the instructions or N to continue to game.\n").upper()
    # print(userscore.cell(3,1).value) this works
    print('')
    while True:
        if answer == "Y":
            instructions()
        elif answer == "N":
            play_game()

        else:
            print('')
            print("Please enter a valid input of either Y or N\n")
            answer = input("").upper()


def instructions():
    """ 
    Game instructions will be printed if the user
    has never played the game.
    """
    clear()
    print(" 1) Game is played against the computer.")
    print(" 2) User enters either 'R'-(Rock) or 'P'-(Paper) or 'S'-(Scissors).")
    print(" 3) Rock wins against scissors.")
    print(" 4) Scissors win against paper.")
    print(" 5) Paper wins against rock.")
    print(" 6) Enter Q to stop the game.")
    print(" 7) Enter C to to clear the console.")
    print(' ')
    time.sleep(8)
    print("Would you like to Play the game or Quit and exit?")
    answer = input("Enter Y to play or N to Quit\n").upper()
    print('')
    while True:
        if answer == "Y":
            play_game()
        elif answer == "N":
            break

        else:
            print('')
            print("Please enter a valid input of either Y to play or N to Quit\n")
            answer = input("").upper()
    clear()


def play_game():
    choice = ["R", "P", "S"]
    computer = choice[randint(0,2)]
    user = input("\u001b[37m\nPlease choose _ R for Rock, P for Paper, and S for Scissors or (Q to quit the game)\n").upper()
    if user == computer:
        print("It's a Draw! ")
        print(userscore.cell(3,1).value)
    elif user == "R":
        if computer == "P":
            print("\u001b[31mYou Lose!")
            print(userscore.cell(3,1).value)
        else:            
            print("\u001b[32mYou Win!")
            print(userscore.cell(3,1).value)
    elif user == "P":
        if computer == "S":
            print("\u001b[31mYou Lose!")
            print(userscore.cell(3,1).value)
        else:
            print("\u001b[32mYou Win!")
            print(userscore.cell(3,1).value)
    elif user == "S":
        if computer == "R":
            print("\u001b[31mYou Lose")
            print(userscore.cell(3,1).value)
        else:            
            print("\u001b[32mYou Win!")
            print(userscore.cell(3,1).value)

    elif user == "Q":
            clear()
            print("Thank you for playing the game.")
            time.sleep(5)
            # intro()
            exit()
    elif user == "C":
            clear()            
    else:
        print("That input isn't valid. Please enter 'R' OR 'P' OR 'S'! Enter Q to quit the game.")


# def get_high_score():
#     """
#     Gets the high score from user who have played the game
#     """
def draw():
    draw += 1
    play_game()

def win():
    wins += 1
    play_game()

def reset():
    wins = 0
    lose = 0
    draw = 0
    userscore.update_cell(3,2, "0")
    userscore.update_cell(3,3, "0")
    userscore.update_cell(3,4, "0")

def clear():
    """
        Clears the screen
    """
    print("\033c")
    
def print_slow(ltr):
    """
    Creates a slow typing effect
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def you_win():
    print(' ')
    print('                     __ __ _____ _____    _ _ _ _____ _____ ')
    print('                    |  |  |     |  |  |  | | | |     |   | |')
    print('                    |_   _|  |  |  |  |  | | | |  |  | | | |')
    print('                      |_| |_____|_____|  |_____|_____|_|___|')
    print(' ')




reset()
intro()
# play_game()
