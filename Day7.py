# number guessing game
import random
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            break
play_game()
