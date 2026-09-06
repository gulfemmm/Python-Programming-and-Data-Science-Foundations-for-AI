import random

# Step 1: Define the math question function
def generate_question():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = num1 + num2

    elif operator == '-':
        answer = num1 - num2

    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

#Step 2: Main Quiz Game Function
def math_quiz():
    score = 0
    rounds = 5
    
    print("\n--- Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems,and you need to provide correct answers.")
    
    for i in range(rounds):
        questioni, correct_aswer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        user_aswer = int(input("Your answer: "))
        
        if user_aswer == correct_aswer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_aswer}")
            
        print("\n--- Game Over! ---")
        print("Your final score is {score}/{rounds}")
        if score == rounds:
            print("Congratulations! You got all the questions correct.")
        elif  score >= rounds // 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing! You can do better next timr.")
            
            
    