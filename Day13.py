# Higher or Lower Game
import random
def main():
    print("Welcome to the Higher or Lower Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number. You have 10 attempts.")
    
    number = random.randint(1, 100)
    attempts = 10
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a valid number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} correctly!")
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Game over! The correct number was {number}.")
if __name__ == "__main__":
    main()
    