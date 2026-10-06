from database import save_candidate, get_candidates, save_result,get_results
from questions import questions
def register_candidate():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    if "@" not in email or "." not in email:
        print("Please enter a valid email.")
        return
    save_candidate(name, email)
    print("\nRegistration successful")
    print("Name:",name)
    print("Email:",email)
    return name, email

def start_test(name, email):
    score = 0
    print("\n===== PYTHON INTERVIEW TEST ======")
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")

        for option in question["options"]:
            print(option)

        answer = input("Enter your answer: ").strip().upper()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    print("\n===== TEST RESULT =====")
    print("Your score:", score, "/", len(questions))

    save_result(name, email, score)

    print("Result saved successfully!")

# Main program
print("===== SMART INTERVIEW EVALUATOR =====")

name, email = register_candidate()

if name is not None and email is not None:
    start_test(name, email)

    print("\n===== REGISTERED CANDIDATES =====")

    candidates = get_candidates()

    for candidate in candidates:
        print(candidate)

print("\n===== TEST RESULTS =====")

results = get_results()

for result in results:
    result_id = result[0]
    name = result[1]
    email = result[2]
    score = result[3]

    percentage = (score / len(questions)) * 100

    print("----------------------------")
    print("ID:", result_id)
    print("Name:", name)
    print("Email:", email)
    print("Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")
    print("----------------------------")
