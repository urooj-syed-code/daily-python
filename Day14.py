# symptom checker game
def main():
    print("Welcome to the Symptom Checker Game!")
    print("I will describe a symptom, and you have to guess the condition.")
    
    symptoms = {
        "Fever, cough, and shortness of breath": "COVID-19",
        "Sneezing, runny nose, and itchy eyes": "Allergy",
        "Chest pain, shortness of breath, and sweating": "Heart Attack",
        "Frequent urination, increased thirst, and fatigue": "Diabetes",
        "Headache, sensitivity to light, and nausea": "Migraine"
    }
    
    for symptom, condition in symptoms.items():
        print(f"Symptom: {symptom}")
        guess = input("Your guess: ")
        
        if guess.lower() == condition.lower():
            print("Correct! Well done!")
        else:
            print(f"Wrong! The correct answer is {condition}.")
    
    print("Game over! Thanks for playing.")
if __name__ == "__main__":
    main()
    