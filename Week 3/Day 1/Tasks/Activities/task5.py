# Activities/Task 5
# Write a program that uses a nested loop to check ,y shopping list against whats in stock at the shop

# Make a list for our shopping lst
shopping_list = ["cheese", "beans", "crisps", "milk", "apples"]

# Make a list of whats in stock at the shop
at_the_shops = ["pears", "jam", "cheese", "apples", "bread", "tuna", "crisps"]

# Check each item in the shopping list against the items at the shops
for item in shopping_list:
    # Make a found bool which will change from TRUE/FALSE depending on the item stock status
    found = False
    # For each item in stock
    for shop_item in at_the_shops:
        # Check if our current item is in stock at the shop
        if item == shop_item:
            # If its in stock it will return true then break the for loop allowing it to run the rest of the code to display if it has been found or not
            found = True
            break
    # Check if our found bool is True if it is we have got the item if not we don't
    if found:
        print(f"Yay, they've got {item}!")
    else:
        print(f"Oh no, they've not got {item}!")

