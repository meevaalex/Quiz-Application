score = 0

print("\n===== PYTHON QUIZ APPLICATION =====")

# QUESTION 1
print("\n1. What does CPU stand for?")
print("a) Central Process Unit")
print("b) Central Processing Unit")
print("c) Computer Personal Unit")
print("d) Central Processor Utility")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == 'b':
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong Answer!")

# QUESTION 2
print("\n2. Which language is used for web development?")
print("a) HTML")
print("b) Python")
print("c) Java")
print("d) C++")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == 'a':
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong Answer!")

# QUESTION 3
print("\n3. Which symbol is used for comments in Python?")
print("a) //")
print("b) <!-- -->")
print("c) #")
print("d) **")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == 'c':
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong Answer!")

# FINAL SCORE
print("\n===== QUIZ COMPLETED =====")
print(f"Your Final Score is: {score}/3")

# PERFORMANCE MESSAGE
if score == 3:
    print("🏆 Excellent!")
elif score == 2:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")