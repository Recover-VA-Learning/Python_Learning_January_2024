import random

def main():
    # Generate random number
    random_number = random.randint(1, 100)
    game_loop(random_number)

def game_loop(random_number):
    guess = get_guess()
    check_guess(guess, random_number)

# ask user for guess
def get_guess():
    # Prompt user for guess from user and return it
    pass # remove this line when you start working on this function

# check if guess is correct
def check_guess(guess, random_number):
    # check if guess in low or high and call game_loop again
    pass # remove this line when you start working on this function

main()