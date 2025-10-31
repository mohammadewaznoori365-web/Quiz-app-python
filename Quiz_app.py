# 📝 Project: Quiz App
# 💻 Language: Python
# 👨‍💻 Author: Mohammad Ewaz,Mohammad omar,Mohammad Abdullah
# 🎯 Purpose: Ask the user 5 quiz questions and show the final score

# ---------------------------------------------------------------
# 🔸 List of questions, options, and correct answers
questions = [
    {
        "question": "1. Who created Python?",
        "options": [
            "1. Elon Musk",
            "2. Guido van Rossum",
            "3. Bill Gates",
            "4. Mark Zuckerberg"
        ],
        "answer": "2"
    },
    {
        "question": "2. When was Python first released?",
        "options": [
            "1. 1989",
            "2. 1991",
            "3. 2000",
            "4. 2010"
        ],
        "answer": "2"
    },
    {
        "question": "3. What symbol is used for comments in Python?",
        "options": [
            "1. //",
            "2. <!-- -->",
            "3. #",
            "4. /* */"
        ],
        "answer": "3"
    },
    {
        "question": "4. Which function is used to print text in Python?",
        "options": [
            "1. echo()",
            "2. print()",
            "3. printf()",
            "4. show()"
        ],
        "answer": "2"
    },
    {
        "question": "5. Which of the following is NOT a Python data type?",
        "options": [
            "1. int",
            "2. str",
            "3. bool",
            "4. real"
        ],
        "answer": "4"
    },
]
# ---------------------------------------------------------------
# 🔸 Initialize score
score = 0
# 🔸 Loop through each question
for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user_answer = input("Enter the number of your answer: ")

    # Check answer
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was option {q['answer']}.\n")

# ---------------------------------------------------------------
# 🔸 Final result
print("🎉 Quiz Finished!")
print(f"Your final score: {score} out of {len(questions)}")