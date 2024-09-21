# Simple Quiz Game

# List of questions and answers
questions = [
    {"question": "What is the capital of Georgia?", "answer": "Tbilisi"},
    {"question": "Who wrote 'Vefxistyaosani'?", "answer": "Shota Rustaveli"},
    {"question": "Who won ucl in 2015", "answer": "Barcelona"},
    {"question": "When did war of didgori happend?", "answer": "1121"},
    {"question": "Who is the GOAT of football?", "answer": "Messi"}
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").strip()
        if answer.lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    print(f"You scored {score} out of {len(questions)}.")

# Start the quiz
if __name__ == "__main__":
    run_quiz(questions)