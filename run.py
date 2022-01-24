quiz_data = [
    {"question": "This dish is a speciality in the region of Gunma, typically consisting of pork\ntenderloin which is breaded and deep fried.",
     "answers": {"A": "Menchikatsu",
                 "B": "Katsudon",
                 "C": "Tonkatsu"},
     "correct_answer": "C"},
    {"question": "A type of sushi, consisting of pressed rice usually topped with fish.",
     "answers": {"A": "Sashimi",
                 "B": "Nigiri",
                 "C": "Maki"},
     "correct_answer": "B"},
    {"question": "These boiled dumplings are usually served in a very light broth, filled with ground meat and vegetables.",
     "answers": {"A": "Yaki gyoza",
                 "B": "Sui gyoza",
                 "C": "Age gyoza"},
     "correct_answer": "B"},

    {"question": "Katsuobushi shavings (or bonito flakes) are derived from which fish?",
     "answers": {"A": "Tuna",
                 "B": "Salmon",
                 "C": "Mackerel"},
     "correct_answer": "A"},
    {"question": "What is Japanese Horseradish also known as?",
     "answers": {"A": "Onigiri",
                 "B": "Karrage",
                 "C": "Wasabi"},
     "correct_answer": "C"},
    {"question": "Found all over Japan in street food markets and sushi restaurants, this fried rolled omelette is typically seasoned with salt and dashi.",
     "answers": {"A": "Tamagoyaki",
                 "B": "Datemaki",
                 "C": "Okonomiyaki"},
     "correct_answer": "A"}, 
    {"question": "Which of the Japanese islands is famous for it’s Tarabagani (King Crab)?",
     "answers": {"A": "Tashiro",
                 "B": "Hokkaido",
                 "C": "Sado"},
     "correct_answer": "B"},
    {"question": "Which Japanese fruit is said to be one of the most expensive in the world?",
     "answers": {"A": "Akebi",
                 "B": "Momo peach",
                 "C": "Yubari melon"},
     "correct_answer": "C"}, 
    {"question": "Which variety of beef is identified by it’s fatty, well-marbled texture?",
     "answers": {"A": "Yonezawa",
                 "B": "Mishima",
                 "C": "Kobe"},
     "correct_answer": "C"}, 
    {"question": "What fish-shaped pancake is traditionally filled with sweetened adzuki beans?",
     "answers": {"A": "Zabuton Dora",
                 "B": "Taiyaki",
                 "C": "Mitarashi Dango"},
     "correct_answer": "B"}
] 

#=====================================================================


def count_keys(quiz_data):
    """
    Counts number of questions in dictionary for the f string on line ENTER LINE NUMBER (this allows more questions 
    to be added to dictionary and the intro text to automatically update with number of questions).
    """
    count = 0
    for i in enumerate(quiz_data):
        count += 1
    return count


num_of_questions = (count_keys(quiz_data))


#=====================================================================

def start_quiz():
    """
    Starting point of quiz, displays ASCII title text and sushi images. Gets user name, shows instructions
    and asks user if they are ready to begin.
    """
    print("""
 _____  ___   ___  ___         ___  _____       ____  ____ ____   ____ ____  __ 
|     |/   \ /   \|   \       /   \|     |     |    |/    |    \ /    |    \|  |
|   __|     |     |    \     |     |   __|     |__  |  o  |  o  |  o  |  _  |  |
|  |_ |  O  |  O  |  D  |    |  O  |  |_       __|  |     |   _/|     |  |  |__|
|   _]|     |     |     |    |     |   _]     /  |  |  _  |  |  |  _  |  |  |__ 
|  |  |     |     |     |    |     |  |       \  `  |  |  |  |  |  |  |  |  |  |
|__|   \___/ \___/|_____|     \___/|__|        \____|__|__|__|  |__|__|__|__|__|
                                                                                

            ,     ,                                    ,,,,,,,,,,,
     ;';' ''''' ;,;        ------;;;;------       ,'' ;  ;  ;  ''|||\//
    ,'  ________  ',      |______|;;|______|      ',,_;__;__;__;,'''/\\
    ;,;'        ';,'        |    |;;|    |         |            |
     '.________.'            '.__|;;|__.'           '.________.'

    \n""")

    global name
    name = input("Please enter you name:\n")

    while name == "" or name == " ":
        print("Please enter your name to begin the quiz\n")
        name = input("Please enter you name:\n")
    else:
        print(f"Welcome to Food of Japan {name}!\n")
        print("Take the quiz to test your knowledge of Japanese cuisine.\n")
        print(f"There are {num_of_questions} multiple choice questions.\n")
        print("Select your answer by typing 'a', 'b' or 'c'.\n")
        print("Good luck!\n")

    begin_quiz = True

    while begin_quiz:
        commence_quiz = input("Are you ready to begin? y/n\n")

        if commence_quiz.lower() == "y":
            print("Lets go\n")
            break
        elif commence_quiz.lower() == "n":
            print("Type 'y' when you are ready to begin\n")
        else:
            print("That is not a valid option\n")

#==================================================================================            


def run_quiz(quiz_data):
    """
    Iterates through quiz questions and potential answers, gets user input and implements score by one or zero, depending on user input. 
    """
    score = 0
    for entry in quiz_data:
        print(f"{entry['question']}")      
        for key, value in entry['answers'].items():
            print(f" \t {key}: {value}")

        user_answer = input("What is your answer?\n")
        user_answer = user_answer.upper()

        if user_answer == entry['correct_answer']:
            print("Correct\n")
            score += 1
        else:
            print("Oops sorry! Better luck next time\n")
            score += 0

    final_score(score)

#=======================================================


def final_score(score):
    """
    Displays final score at end of quiz
    """
    print(f"Congratulations {name}! Your final score is {score} out of 10")

#=======================================================


def play_again():
    """
    Asks user if they want to play again. Returns to start of quiz, or ends quiz depending on user input
    """
    response = input("Do you want to play again? y/n\n")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False


start_quiz()
run_quiz(quiz_data)

while play_again():
    start_quiz()
    run_quiz(quiz_data)
else:
    print("end of quiz")
