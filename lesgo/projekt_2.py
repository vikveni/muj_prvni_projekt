

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Viktor Veniger
email: viktorveniger@gmail.com
discord: VikVeni#8755
"""
import random
secret_number = []
separator = "-" * 47

def intro():
    print("Hi there!",
          separator,
          "I've generated a random 4 digit number for you. ",
          "Let's play a bulls and cows game.",
          separator,
          sep="\n"
          )

def random_secret_number():
    while len(secret_number) != 4:
        secret_number.append(random.randrange(0, 9))
        if len(secret_number) > len(set(secret_number)) or secret_number[0] == 0:
            secret_number.clear()
    return secret_number

def bulls_cows():
    bulls = 0
    cows = 0
    guess = []
    choice = input("Enter a number: ")
    for i in range(4):
        guess.append(int(choice[i]))
        for x in range(4):
            if guess[i] == secret_number[x]:
                cows += 1
        if guess[i] == secret_number[i]:
            bulls += 1
            cows -= 1
    if bulls == 4:
        print(f"Congratualtions you are the winner, the number was {secret_number}")
        quit()
    print(f"{bulls} bulls, {cows} cows")
    print(separator)
    bulls_cows()

def game_player():
    random_secret_number()
    bulls_cows()

game_player()

