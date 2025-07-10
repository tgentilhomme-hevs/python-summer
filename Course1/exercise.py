
print("Welcome to the Python Quiz!")

name = input("What's your name? ")
print("Hi", name + "!", "Let's begin.\n")

score = 0

questions = [
    "What is 2 + 2?",
    "What is the capital of France?",
    "What returns \"python\".upper() do in Python?"
]

answers = [
    "4",
    "paris",
    "PYTHON"
]

for i, q in enumerate(questions):
    answer = input(q + " ").lower()
    if answers[i].lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print("You got", score, "out of", len(questions))
if score == 3:
    print("Perfect score! Great job,", name.upper() + "!")
elif score > 0:
    print("Not bad! Try again to improve.")
else:
    print("Keep practicing!")
