"""
----Activity

Your task is to create a Python Console app version of
the 'Rock Paper Scissors' game.

The user will be playing against the computer which will
randomly share one of the three outcomes after the
user has entered their choice.

The round will then end, and the result shown to the
user.

----Extras

(*) Make the game more visual in the console by using ASCII art library or other characters.
(*) Best out of 3, 5 or 7? 
Add functionality so that the user can play more than one game.

"""


import random
from colorama import Fore, Style

# ascii art for the rps game
ascii_art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

# just something to keep the console nice
rpsI = f"[{Fore.CYAN}i{Style.RESET_ALL}]"
rpsU = f"[{Fore.BLACK}U{Style.RESET_ALL}]"
rpsS = f"[{Fore.GREEN}U{Style.RESET_ALL}]"
rpsT = f"[{Fore.YELLOW}i{Style.RESET_ALL}]"
rpsC = f"[{Fore.RED}C{Style.RESET_ALL}]"

def get_computer_choice():
    # randomly choose between rock, paper, and scissors
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # get the users choice and validate input
    user_input = input(f"{rpsU} Enter your choice (rock, paper, scissors): ").strip().lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print(f"{rpsU} Invalid choice. Please try again.")
        user_input = input(f"{rpsU} Enter your choice (rock, paper, scissors): ").strip().lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    # basic rps rules evaluation
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def play_round():
    # start a round of rps
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\n{rpsU} You chose:\n{ascii_art[user_choice]}")
    print(f"{rpsI} Computer chose:\n{ascii_art[computer_choice]}")
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print(f"{rpsT} It's a tie!")
    elif result == "user":
        print(f"{rpsS} You win!")
    else:
        print(f"{rpsC} Computer wins!")
    return result

def rps():
    while True:
        # ask how many rounds they want to play 3, 5, 7
        best_of = int(input(f"{rpsI} Best of how many rounds? (3, 5, or 7): ").strip())
        while best_of not in [3, 5, 7]:
            print(f"{rpsU} Invalid choice. Please enter 3, 5, or 7.")
            best_of = int(input(f"{rpsI} Best of how many rounds? (3, 5, or 7): ").strip())

        # calc number of wins to win the series
        required_wins = (best_of // 2) + 1
        user_wins = 0
        computer_wins = 0

        # keep playing until someone wins the series
        while user_wins < required_wins and computer_wins < required_wins:
            result = play_round()
            if result == "user":
                user_wins += 1
            elif result == "computer":
                computer_wins += 1
            print(f"{rpsI} Score: You {user_wins} - {computer_wins} Computer\n")

        # print the winner
        if user_wins > computer_wins:
            print(f"{rpsS} Congratulations! You won the best of {best_of} series!")
        else:
            print(f"{rpsC} Sorry! The computer won the best of {best_of} series!")

        # see if they want to play again
        play_again = input(f"{rpsI} Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"{rpsI} Thanks for playing!")
            break

# Start our game
rps()
