def favorite_books():
    # List of my favorite books
    my_favorite_books = [
        "Scorpia",
        "Stormbreaker",
        "Point Blanc",
        "Bloody Horowitz",
        "Horowitz Horror"
    ]
    
    # Input from user
    while True:
        user_input = input("Enter the title of your favorite book (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if user_input == '':
            print("Please enter a valid book title.")
            continue
        
        # Checking if user's favorite book matches my favorite books
        if user_input in my_favorite_books:
            print(f"{user_input} is one of my favorite books too.")
        else:
            print("I haven't read that book.")

# Running the program
favorite_books()
