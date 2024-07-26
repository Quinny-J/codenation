import random

def play_game():
    score = 0
    while True:
        input("Press Enter to roll the dice ... ")
        
        # Roll the dice (generate a random number between 1 and 6)
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}.")
        
        if roll == 1:
            print("Sorry, you rolled a 1. Your score has been reset.")
            score = 0
            break  # End the game
        else:
            score += roll
            print(f"Your current score is {score}.")
        
        # Check if the score has reached or exceeded 20
        if score >= 20:
            print("Congratulations! You've reached a score of 20 or more.")
            break  # End the game
        
        # Optionally, you can ask if the user wants to continue playing
        continue_game = input("Do you want to roll again? (y/n): ")
        if continue_game.lower() != 'y':
            break

    print(f"Game over. Your final score is {score}.")

# Start the game
play_game()
