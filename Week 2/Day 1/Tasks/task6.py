#
# Task 6 Stretch
# Create a var called word and check for paladrome

word = "racecar"
# Splice our word var backwards and make it a var
# reversed_word = reversed(word)
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is the same forwards and backwards")
else:
    print(f"{word} is not the same forwards and backwards")