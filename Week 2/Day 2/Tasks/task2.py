# Task 2
# Copy the shopping list and use a method to display the number of the items (egg, kale, stamps, carrot, orange juice)

# Create our shopping string list
shopping_list = [
"apple",
"carrot",
"pizza",
"carrot",
"dog food",
"orange juice",
"egg",
"kale",
"carrot",
"kale",
"orange juice",
"kale",
"toilet roll",
"stamps",
"noodles",
"pasta sauce",
"egg",
"pasta sauce"
]

# Create our shopping items item counts in a dict egg:2 var:value
shopping_item_count = {}

# Check each item in our shopping list and count it
for item in shopping_list:
    if item in shopping_item_count:
        shopping_item_count[item] += 1
    else:
        shopping_item_count[item] = 1

# List of items we want the count for
items_to_count = ["egg", "kale", "stamps", "carrot", "orange juice"]

# Display the number of items based of our count dict
for item in items_to_count:
    print(f"{item}: {shopping_item_count.get(item, 0)}")

print(shopping_item_count)
