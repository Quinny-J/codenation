# Write a program which lets the user type in an item and
# adds it to a shopping list.

# If the item is already on the list, do not allow it to be
# added again.

shopping_list = []

def add_item_to_list(item, shopping_list):
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"I have added {item} to your list")
    else:
        print(f"Im sorry but the item has already been added")

while True:
    item = input("Please enter a item you would like to add to your shopping list : ")

    if not item:
        break

    add_item_to_list(item, shopping_list)

    print("Your shopping list")
    print(shopping_list)