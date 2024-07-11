# Task 3
# Use the two lists to create a dict where country is key and value is language

# Create a dict with animal names
animals = {
    "Lion": "Cub",
    "Pigeon": "Squab",
    "Gecko": "Hatchling",
    "Hedgehog": "Hoglet",
}

# Function to handle input
def submit_animal():
    # take users input
    animal = input("Enter the animal name: ")
    baby_name = input("Enter the baby name: ")
    
    # check if animal exists in our dict if so do appropriate action
    if animal in animals:
        print(f"The baby name for {animal} is {animals[animal]}.")
    else:
        animals[animal] = baby_name
        print(f"Added {animal} with baby name {baby_name} to the dictionary.")

# Run the function to allow user input
submit_animal()

# Print the updated dictionary
print("Updated dictionary:", animals)
