# dice battle
import random
def roll_dice():
    return random.randint(1, 6)
def main():
    print("Welcome to the Dice Battle!")
    player_score = 0
    computer_score = 0
    for round in range(1, 6):
        input(f"Round {round}: Press Enter to roll the dice...")
        player_roll = roll_dice()
        computer_roll = roll_dice()
        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")
        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1
        elif computer_roll > player_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
    print("\nFinal Scores:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("The game is a tie!")
if __name__ == "__main__":
    main()
    