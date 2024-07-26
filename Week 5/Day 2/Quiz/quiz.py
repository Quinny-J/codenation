import random
from colorama import Fore, Style

def get_username(input_func=input):
    return input_func("Please enter your user name here: ")

def initialize_high_scores_file():
    try:
        with open('high-scores.txt', 'x') as f:
            f.write('Username: Score\n')
    except FileExistsError:
        pass

def shuffle_questions(questions):
    keys = list(questions.keys())
    random.shuffle(keys)
    return keys

def ask_question(question, choices, input_func=input):
    print(f"{question}")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
    
    while True:
        user_input = input_func("Please enter your answer (1, 2, 3, 4): ")
        if user_input not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
            print(Style.RESET_ALL)
        else:
            return int(user_input)

def update_score(is_correct, current_score):
    if is_correct:
        return current_score + 5
    else:
        return current_score - 2

def display_feedback(is_correct, choices, correct_answer):
    if is_correct:
        print(f"{Fore.GREEN}Correct answer: {choices[correct_answer - 1]}\n")
    else:
        print(f"{Fore.RED}Incorrect. The correct answer is: {choices[correct_answer - 1]}\n")
    print(Style.RESET_ALL)

def save_score(username, score, filename='high-scores.txt'):
    with open(filename, 'a') as f:
        f.write(f'Username: {username}, Score: {score}\n')

def display_high_scores(filename='high-scores.txt'):
    print("\nHigh Scores:")
    with open(filename, 'r') as f:
        for line in f:
            if line.strip() and 'Username' in line:  # Skip the header line
                continue
            parts = line.strip().split(', ')
            username = parts[0].split(': ')[1]
            score = int(parts[1].split(': ')[1])
            print(f"{Fore.GREEN}{username} {Fore.YELLOW}{score}")
    print(Style.RESET_ALL)

def main(input_func=input):
    user_score = 0
    quiz_questions = {
        "Question_1": {
            "Question_Type": "Who scored the most goals in a World Cup?",
            "Choice": ["Miroslav Klose", "Cristiano Ronaldo", "Leo Messi", "Eric Cantona"],
            "Answer": 1
        },
        "Question_2": {
            "Question_Type": "What's the hottest place in the world?",
            "Choice": ["Sitka, ALASKA", "Palermo, ITALY", "Death Valley, USA", "Brighton, UK"],
            "Answer": 3
        },
        "Question_3": {
            "Question_Type": "Who is the fastest man in the world?",
            "Choice": ["Tyson GAY", "Usain St. Leo Bolt OJ", "Asafa POWELL, USA", "Trayvon BROMELL"],
            "Answer": 2
        },
        "Question_4": {
            "Question_Type": "What is the 3rd highest mountain in the world?",
            "Choice": ["Everest", "K2", "Fujiama", "Kangchenjunga"],
            "Answer": 4
        },
        "Question_5": {
            "Question_Type": "What is the fastest airplane in the world?",
            "Choice": ["Lockheed SR-71 Blackbird", "NASA X-43A", "Lockheed YF-12", "Mikoyan-Gurevich MiG-25 Foxbat"],
            "Answer": 2
        }
    }

    username = get_username(input_func)
    initialize_high_scores_file()
    shuffled_keys = shuffle_questions(quiz_questions)

    for key in shuffled_keys:
        question = quiz_questions[key]
        user_answer = ask_question(question["Question_Type"], question["Choice"], input_func)
        is_correct = user_answer == question["Answer"]
        user_score = update_score(is_correct, user_score)
        display_feedback(is_correct, question["Choice"], question["Answer"])

    save_score(username, user_score)
    print(f"User score is {user_score}")
    display_high_scores()

if __name__ == "__main__":
    main()
