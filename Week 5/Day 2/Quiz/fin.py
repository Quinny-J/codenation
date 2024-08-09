# Import Modules
import random
from colorama import Fore, Style
 
# User score variable
user_score = 0
 
# quiz dict
quiz_questions = {
   
    "Question_1":
    {
        "Question_Type" : "Who scored the most goals in a World Cup?",
        "Choice" : ["1.Miroslav Klose","2.Cristiano Ronaldo", "3.Leo Messi", "4.Eric Cantona"],
        "Answer" : 1
    },
 
    "Question_2":
    {
        "Question_Type" : "What's the hottest place in the world?",
        "Choice" : ["Sitka, ALASKA,","Palermo, ITALY", "Death Valley, USA", "Brighton, UK"],
        "Answer" : 3
    },
    
    "Question_3":
        {
        "Question_Type" : "Who is the fastest man in the world?",
        "Choice" : ["Tyson GAY,","Usain St. Leo Bolt OJ", "Asafa POWELL, USA", "Trayvon BROMELL"],
        "Answer" : 2
            
        },
    "Question_4":
        {
        "Question_Type" : "What is  3rd hightest mountain in the world?",
        "Choice" : ["Everest,","K2","Fujiama","Kangchenjunga"],
        "Answer" : 4
        },
        
    "Question_5":
        {
        "Question_Type" : "What is the fastest airplane in the world?",
        "Choice" : ["Lockheed SR-71 Blackbird","NASA X-43A","Lockheed YF-12","Mikoyan-Gurevich MiG-25 Foxbat"],
        "Answer" : 2
        }
             
 
}
 
# Create a new list called question_keys with random keys form the dict keys
question_keys = list(quiz_questions.keys()) #We had to goole it
random.shuffle(question_keys) #We had to goole it
 
# Take username from input
username = input("Please enter your user name here: ")
 
# Try to open and write to high-scores if not handle the error
try:
    with open('high-scores.txt', 'x') as f:
        f.write(f'Username: {username}, Score: 0\n')
except FileExistsError: # we had to google it kept causing error when file was not created
    pass

# Loop through the random question keys 
for key in question_keys:
    value = quiz_questions[key]
    #print(f"{key.capitalize()}: {value['Question_Type']}")

    # Print each choice from the dict
    for choice in value['Choice']:
        print(choice)
   
   # Keep them in a loop so they play until the end
    while True:
        myInput = input("Please enter your answer (1, 2, 3, 4): ")
        # Check if supplied input is a number from 1-4
        if myInput not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
            print(Style.RESET_ALL)
        else:
            # Convert input from str to int
            myInput = int(myInput)
            if myInput == value['Answer']:
                print(f"{Fore.GREEN} Correct answer: {value['Choice'][value['Answer'] - 1]}\n")
                print(Style.RESET_ALL)
                # Correct +5 Score
                user_score +=5
            else:
                print(f"{Fore.RED}Incorrect. The correct answer is: {value['Choice'][value['Answer'] - 1]}\n")
                print(Style.RESET_ALL)
                # Incorrect +5 Score
                user_score -=2
            break
 
# Write the scores the the file
with open('high-scores.txt', 'a') as f:
        f.write('Username: {0}, Score: {1}\n'.format(username, user_score))
        print(f"User score is {user_score}")
 
# Read the scores and split them into separate vars 
with open('high-scores.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(', ') # Split ,
            username = parts[0].split(': ')[1] # Username
            score = int(parts[1].split(': ')[1]) # Score
            print(f"{Fore.GREEN}{username} {Fore.YELLOW}{score}")