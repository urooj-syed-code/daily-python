# Dice rolling game
import random
def roll_dice():
    dice = random.randint(1, 6)
    return dice
def play_game():
    user_choice = int(input("Choose a number between 1 and 6: "))
    dice_result = roll_dice()
    print(f"The dice rolled: {dice_result}")
    if user_choice == dice_result:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Try again!")
play_game()
