# Activities/Task 4
# Write a program that uses a for loop to check if each element is a dog if it is add it to a new list and then print out the length of the list

# make a list for our animals
animals = ["cat", "dOg", "DOG", "bird", "elephant", "Jim", "dog"]

# New list to store dogs
dogs = []

# Check the original list and check for "dog"
for animal in animals:
    # If our original list item  == dog then add it to the dog list
    if animal.lower() == "dog":
        dogs.append(animal)

# Print the count of dogs by getting the lengths of the new list using a fstring
print(f"We have {len(dogs)} dogs at our shelter.")

