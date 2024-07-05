
#
# Task 5
# Check if the word starts and end with the same letters

word = "RaCecar".lower()
#word = input("Please enter a word to check: ").lower().strip()

if word[0] == word[-1]:
    print(f"{word} starts and ends with {word[0]}")
else:
    print(f"{word} does not start and end with the same letter")
