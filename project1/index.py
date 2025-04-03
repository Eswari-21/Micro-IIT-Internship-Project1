import random
import time

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is referred to as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who is the author of 'To Kill a Mockingbird'?",
        "choices": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"], 
        "answer": "Harper Lee"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Au", "Ag", "Pb", "Fe"],
        "answer": "Au"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "choices": ["India", "China", "Japan", "Russia"],
        "answer": "China"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Which is the longest river in the world?",
        "choices": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    }
]

random.shuffle(questions)
score = 0
total_questions = len(questions)

def load_question(index):
    if index < total_questions:
        question_obj = questions[index]
        print("\n"+ "="*70)
        print(f"Q{index + 1}: {question_obj['question']}")
        for idx, choice in enumerate(question_obj['choices'], 1):
            print(f"{idx}. {choice}")
        return True
    else:
        print("\n" + "="*70)
        print(f"Game Over! Your final score is {score}/{total_questions}")
        print("Thanks for playing! ????")
        return False

def check_answer(index, user_choice):
    global score
    question_obj = questions[index]
    if question_obj['choices'][user_choice - 1] == question_obj['answer']:
        print("✅ Correct!...🎉🎉🎉")
        score += 1
    else:
          print(f"❌ Wrong!...😔😔😔 The correct answer was: {question_obj['answer']}")
    time.sleep(1)

print("Welcome to the Quiz Game! ????")
print("Answer the questions by typing the correct option number. Good luck!")
    

for i in range(total_questions):
    if not load_question(i):
        break
    while True:
         try:
            user_input = int(input("Enter your answer (1-4): "))
            if user_input in [1, 2, 3, 4]:
                check_answer(i, user_input)
                break
            else:
                print("⚠️ Please enter a number between 1 and 4.")
         except ValueError:
             print("⚠️ Invalid input. Enter a number between 1 and 4.")