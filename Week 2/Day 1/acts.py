#
# Task 1
# Create a var called password and check how many letters if has min 8

passwords = ["advg", "acbredgyrw"]

# You could swap this for a input so you can check users passsword but instead lets chack a few passwords
for i in passwords:
    # Check min length of 8
    if len(i) >= 8:
        # Print result
        print(f"{i} is a great password")
    else:
        # Print result
        print(f"{i} is too short to be a password")

#
# Task 2
# Create a var called num and check if can be div by 3 or 5
num = 10

# Check if the num var has a number that can be divided by 3 or 5
# We need to divide the number and check if it returns 0 then it can be divided if not return message
if num % 5 == 0 or num % 3 == 0:
    print(f"{num} can be divided by 3 or 5")
else:
    print(f"{num} can not be divided by 3 or 5")


#
# Task 3
# Create a var called num and check if can be div by 3 or 7
num = 70 # 21 can be divised by both

# Check if the num var has a number that can be divided by 3 or 7
# We need to divide the number and check if it returns 0 then it can be divided if not return message
if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz")
elif num % 3 == 0: 
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(f"{num} can not be divided by 3 or 7")

#
# Task 4
# England captial make is so london and London get accepted as answers
print("What is the capital of England?")

answer = input("Type your answer here: ") # You can put .lower here or in the if statement

if answer.lower() == "london":
    print(f"Correct! The answer is {answer}")
else:
    print(f"Incorrect! The answer is 'London', not {answer}")

#
# Task 5
# Check if the word starts and end with the same letters

word = "racecar"

if word[0] == word[-1]:
    print(f"{word} starts and ends with {word[0]}")
else:
    print(f"{word} does not start and end with the same letter")

#
# Task 6 Stretch
# Create a var called word and check for paladrome

word = "racecar"
# Splice our word var backwards and make it a var
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is the same forwards and backwards")
else:
    print(f"{word} is not the same forwards and backwards")