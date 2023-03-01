questions = {
    "question1": {
        "question": "What color is a banana?",
        "answer": "Yellow"
    },
    "question2": {
        "question": "Where is Paris?",
        "answer": "France"
    },
    "question3": {
        "question": "What is the capital of Portugal",
        "answer": "Lisbon"
    }
}

score = 0

for key, value in questions.items():
    print(value["question"])
    answer = input("Answer: ")

    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score += 1
        print(f"Your score is: {score}")
    else:
        print("Wrong!")
        print(f"The answer is: {value['answer']}")
        print(f"Your score is: {score}")

print(f"Game over! Your final score is: {score}")