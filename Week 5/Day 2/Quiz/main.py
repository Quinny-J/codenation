import random


user_score = 0

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


#print(quiz_questions["Question_Type"]["Choice"])


username = input("Please enter your username : ")


try:
    with open('high-scores.txt', 'x') as f: 
        f.write(f'Username: {username}, Score: 0\n')
except FileExistsError:
    pass 


question_keys = list(quiz_questions.keys())
random.shuffle(question_keys)

for key, value in quiz_questions.items():
    print(f"{key.capitalize()}: {value['Question_Type']}")
    for choice in value['Choice']:
        print(choice)
    
    while True:
        myInput = input("Please enter your answer (1, 2, 3, 4): ")
        if myInput not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4.")
        else:
            myInput = int(myInput)
            if myInput == value['Answer']:
                print(f"Correct answer: {value['Choice'][value['Answer'] - 1]}\n")
                user_score += 5
            else:
                print(f"Incorrect. The correct answer is: {value['Choice'][value['Answer'] - 1]}\n")
                user_score -= 2
            break

print(f"User score : {user_score}")   
print(f"Prev score : {user_score}")   


with open('high-scores.txt', 'a') as f:
        f.read('Username: {0}, Score: {1}\n'.format(username, user_score))

with open('high-scores.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(', ') # Split , 
            username = parts[0].split(': ')[1] # Username
            score = int(parts[1].split(': ')[1]) # Score
            print(f"{username} {score}")

