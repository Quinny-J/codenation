import random
from colorama import Fore, Style

# Define a dictionary of fortunes
fortunes = {
    "good": [
        "It is certain.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes."
    ],
    "bad": [
        "Don't count on it.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "No.",
        "Not likely.",
        "Ask again later."
    ]
}

def magic_8_ball():
    # Ask user for a question
    question = input("Ask the Magic 8 Ball a question: ")

    # Generate a random number
    random_number = random.randint(1, 100)

    # Determine if the random number is odd or even
    if random_number % 2 == 0:  # Even number
        fortune_type = "good"
    else:  # Odd number
        fortune_type = "bad"

    # Select a random fortune from the chosen type
    fortune = random.choice(fortunes[fortune_type])

    # Print the fortune with appropriate color
    if fortune_type == "good":
        print(f"{Fore.GREEN}{fortune}{Fore.WHITE}")
    else:
        print(f"{Fore.RED}{fortune}{Fore.WHITE}")

def m8_ball_loop():
    while True:
        magic_8_ball()
        play_again = input("Do you want to ask another question? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

m8_ball_loop()
