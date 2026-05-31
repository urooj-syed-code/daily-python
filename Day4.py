# coin toss game
import random
def coin_toss():
    toss = random.choice(['Heads', 'Tails'])
    return toss
def play_game():
    user_choice = input("Choose Heads or Tails: ")
    toss_result = coin_toss()
    print(f"The coin toss result is: {toss_result}")
    if user_choice == toss_result:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Try again!")
play_game()
