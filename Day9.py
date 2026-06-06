# word scramble game
import random
def get_user_guess():
    while True:
        guess = input("Your guess: ").strip().lower()
        if guess:
            return guess
        else:
            print("Please enter a valid guess.")
def play_word_scramble_game():
    words = ["python", "programming", "challenge", "developer", "algorithm"]
    word = random.choice(words)
    scrambled_word = ''.join(random.sample(word, len(word)))
    print(f"Scrambled word: {scrambled_word}")
    user_guess = get_user_guess()
    if user_guess == word:
        print("Correct! You guessed the word.")
    else:
        print(f"Wrong! The correct word was: {word}")
play_word_scramble_game()
