# پروژه: quiz_app (برنامه سوال و جواب)
#ترتیب کننده: محمد عوض,محمد عمر و محمد عبدالله
#هدف: پرسیدن چمد سوال از کاربر و نمایش امتیاز نهایی
#توضیح:
#این برنامه شامل پنج سوال چهار گزینه ای است
score = 0
print("Please type the number (1-4) of your correct answer.\n")

# Question 1
print("1. Who created the Python programming language?")
print("1) Elon Musk")
print("2) Guido Van Rossum")
print("3) Bill Gates")
print("4) Mark Zuckerberg")
ans = input("Enter your answer (1-4): ")
if ans == "2":
    score += 1

# Question 2
print("\n2. In which year was Python first released?")
print("1) 1989")
print("2) 2000")
print("3) 1991")
print("4) 2010")
ans = input("Enter your answer (1-4): ")
if ans == "3":
    score += 1

# Question 3
print("\n3. What symbol is used for writing comments in Python?")
print("1) //")
print("2) #")
print("3) < !-- -->")
print("4) **")
ans = input("Enter your answer (1-4): ")
if ans == "2":
    score += 1

# Question 4
print("\n4. Which Python function is used to print text on the screen?")
print("1) echo()")
print("2) print()")
print("3) show()")
print("4) printf()")
ans = input("Enter your answer (1-4): ")
if ans == "2":
    score += 1

# Question 5
print("\n5. Which of the following is NOT a Python data type?")
print("1) int")
print("2) str")
print("3) bool")
print("4) real")
ans = input("Enter your answer (1-4): ")
if ans == "4":
    score += 1
# نتیجه نهایی
print("🎯 Quiz Finished!")
print(f"Your final score is: {score} out of 5")