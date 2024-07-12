# Tasks/Activities/Act4
# Define a function called count_vowels(word) that takes a word as input and
# prints the count of vowels (a, e, i, o, u) in the word.

def count_vowels(word):
    vowels = 'aeiou'
    # vowelsList = ['a', 'e', 'i', 'o', 'u'] # Unused for this method
    count = 0
    for letter in word.lower():
        if letter in vowels: # Could use vowelList instead
            count += 1

    print(f"The number of vowels in {word} is {count}")

count_vowels("MuRdOcK")
count_vowels("Python")
