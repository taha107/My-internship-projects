# Define your questions, options, and correct answers
questions = [
    {
        'question': 'Question 1: What is the capital of India?',
        'options': ['A. Mumbai', 'B. New Delhi', 'C. Kolkata', 'D. Chennai'],
        'correct_answer': 'B'
    },
    {
        'question': 'Question 2: Which planet is known as the Red Planet?',
        'options': ['A. Mars', 'B. Venus', 'C. Jupiter', 'D. Saturn'],
        'correct_answer': 'A'
    },
    {
        'question': 'Question 3: Who painted the Mona Lisa?',
        'options': ['A. Pablo Picasso', 'B. Leonardo da Vinci', 'C. Vincent van Gogh', 'D. Michelangelo'],
        'correct_answer': 'B'
    }
]

# Initialize score
score = 0

# Define a function to ask questions and get user input
def ask_question(question):
    print(question['question'])
    for option in question['options']:
        print(option)
    user_answer = input('Enter your answer (A, B, C, or D): ')
    return user_answer.upper()

# Iterate through each question
for question in questions:
    user_choice = ask_question(question)
    if user_choice == question['correct_answer']:
        print('Correct answer!')
        score += 1
    else:
        print('Incorrect answer. The correct answer is', question['correct_answer'])

# Display final score
print('Quiz completed. Your final score is', score, 'out of', len(questions))