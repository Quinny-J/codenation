#
# Task 4
# England captial make is so london and London get accepted as answers
print("What is the capital of England?")

answer = input("Type your answer here: ").lower().strip()

if answer == "london": # You can put .lower here or in the if statement
    print(f"Correct! The answer is {answer}")
else:
    print(f"Incorrect! The answer is 'London', not {answer}")