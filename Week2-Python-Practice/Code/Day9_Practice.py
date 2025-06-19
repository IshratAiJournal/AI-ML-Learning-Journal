# Building a multiple choice quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
question_prompts = [
    "1. What color are bananas?\n(a) Red\n(b) Yellow\n(c) Blue\n(d) Green\n\n",
    "2. Which animal barks?\n(a) Cat\n(b) Cow\n(c) Dog\n(d) Sheep\n\n",
    "3. What is 2+2?\n(a) 3\n(b) 4\n(c) 5\n(d) 7\n\n"                 
]

questions = [
    Question(question_prompts[0], 'b'), 
    Question(question_prompts[1], 'c'), 
    Question(question_prompts[2], 'b'),          
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Oops! Wrong answer.\n")
    print(f"You got{score}/{len(questions)} correct! 🎉")

run_quiz(questions)


# One more option with different message

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "1. What color are bananas?\n(a) Red\n(b) Yellow\n(c) Blue\n(d) Green\n\n",
    "2. Which animal barks?\n(a) Cat\n(b) Cow\n(c) Dog\n(d) Sheep\n\n",
    "3. What is 2+2?\n(a) 3\n(b) 4\n(c) 5\n(d) 7\n\n"                 
]

questions = [
    Question(question_prompts[0], 'b'), 
    Question(question_prompts[1], 'c'), 
    Question(question_prompts[2], 'b'),          
]

def run_quiz(questions):
    print("🎉 Welcome to the Ultimate Fun Quiz!🎉")
    name = input("👦What is your name?")
    print(f"\nHi {name}! Let's begin...\n")

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("✅correct!\n")
            score += 1

        else:
            print("❌ Oops! That's not right.\n")

    print(f"🎯Quiz Over, {name}!")
    print(f"You got {score} out of {len(questions)} correct!")

    if score == len(questions):
        print("🏆 You're a genious! Full marks!💯")
    elif score == len(questions) - 1:
        print("👏 Great job! Just missed one!")
    elif score == 1:
        print("😀 You got one! Practice makes perfect!")
    else:
        print("😅 It's okay! try again and you will rock it next time!")

run_quiz(questions)
