import random

def main():
    random_number = random.randint(1, 100)
    game_loop(random_number)

def game_loop(random_number):
    guess = get_guess()
    check_guess(guess, random_number)

# ask user for guess
def get_guess():
    guess = int(input("Guess a number between 1 and 100: "))
    return guess

# check if guess is correct
def check_guess(guess, random_number):
    if guess < random_number:
        print(">>> Too low! <<<")
        game_loop(random_number)
    elif guess > random_number:
        print(">> Too high! <<<")
        game_loop(random_number)
    else:
        print(">>> You guessed correctly! <<<")

main()