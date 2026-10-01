## Name: David Perera
# Student ID: 884532367
# Section: 07
# Assignment: Module 5 Assignment 3

triviabank_dict = {}

print("Welcome to the trivia builder 3000")

question_str = True
while question_str != "Done":
        question_str = input(f"Enter the next question: ")
        if question_str == "Done":
            break
        elif question_str == "":
            print(f"You did not enter a question, let's try again.")
            continue
        answer_str = input(f"Enter the correct answer to that question: ")
        triviabank_dict[question_str] = answer_str
print(f"We will stop entering questions now")
print(f"Here is the final trivia dictionary: ")
for question, answer_str in triviabank_dict.items():
    print(f"The question is: {question}")
    print(f"And the answer is: {answer_str}")
