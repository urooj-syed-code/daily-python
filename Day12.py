# port guessing game
import random
def main():
    print("Welcome to the port guessing game!")
    print("I have selected a random port number between 1 and 65535.")
    print("Try to guess the port number. You have 10 attempts.")
    
    port_number = random.randint(1, 65535)
    attempts = 10
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 65535:
                print("Please enter a valid port number between 1 and 65535.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < port_number:
            print("Too low! Try again.")
        elif guess > port_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the port number {port_number} correctly!")
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Game over! The correct port number was {port_number}.")
if __name__ == "__main__":
    main()
    