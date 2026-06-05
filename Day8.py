# python trivia game
import random
def get_user_answer():    
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer:
            return answer
        else:
            print("Please enter a valid answer.")
def play_trivia_game():
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "harper lee"},
        {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "Who painted the Mona Lisa?", "answer": "leonardo da vinci"}
    ]
    random.shuffle(questions)
    score = 0
    for q in questions:
        print(q["question"])
        user_answer = get_user_answer()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")
    print(f"Your final score is: {score}/{len(questions)}")
play_trivia_game()
