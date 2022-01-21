quiz_data = [
    {"question": "This dish is a speciality in the region of Gunma, typically consisting of pork tenderloin which is breaded and deep fried.",
     "answers": {"A": "Menchikatsu",
                 "B": "Katsudon",
                 "C": "Tonkatsu"},
     "correct_answer": "C"},
    {"question": "A type of sushi, consisting of pressed rice usually topped with fish.",
     "answers": {"A": "Sashimi",
                 "B": "Nigiri",
                 "C": "Maki"},
     "correct_answer": "B"},
    {"question": "What is your name?",
     "answers": {"A": "Tom",
                 "B": "Harry",
                 "C": "Leah"},
     "correct_answer": "C"},
]

#=====================================================================

def start_quiz():
    """
    Starting point of quiz, displays ASCII title text and sushi images. Gets user name, shows instructions and asks user if 
    they are ready to begin. 
    """
    print("""
    _____   ___    ___   ___         ___   _____       ____   ____  ____   ____  ____   __ 
    |     | /   \  /   \ |   \       /   \ |     |     |    | /    ||    \ /    ||    \ |  |
    |   __||     ||     ||    \     |     ||   __|     |__  ||  o  ||  o  )  o  ||  _  ||  |
    |  |_  |  O  ||  O  ||  D  |    |  O  ||  |_       __|  ||     ||   _/|     ||  |  ||__|
    |   _] |     ||     ||     |    |     ||   _]     /  |  ||  _  ||  |  |  _  ||  |  | __ 
    |  |   |     ||     ||     |    |     ||  |       \  `  ||  |  ||  |  |  |  ||  |  ||  |
    |__|    \___/  \___/ |_____|     \___/ |__|        \____j|__|__||__|  |__|__||__|__||__|

                    ,     ,                                    ,,,,,,,,,,,
             ;';' ''''' ;,;        ------;;;;------       ,'' ;  ;  ;  ''|||\//
            ,'  ________  ',      |______|;;|______|      ',,_;__;__;__;,'''/\\
            ;,;'        ';,'        |    |;;|    |         |            |
             '.________.'            '.__|;;|__.'           '.________.'
 
    \n""")

    #global name 
    name = input("Please enter you name:\n")
    while name == "" or name == " ":
        print("Please enter your name to begin the quiz")
        name = input("Please enter you name:\n")
        break
    else:
        print(f"\nWelcome to Food of Japan {name}!\n")
        print("Take the quiz to test your knowledge of Japanese cuisine.\n")
        print("There are 10 multiple choice questions, good luck!\n")

    start_quiz = True

    while start_quiz:
        commence_quiz = input("Are you ready to begin? y/n ")

        if commence_quiz.lower() == "y":
            print("Lets go")
            break
        elif commence_quiz.lower() == "n":
            print("Oh no")
        else:
            print("That is not a valid option")

#==================================================================================            

def run_quiz(quiz_data):
    for entry in quiz_data:
        print(f"Question:{entry['question']}")
        for key, value in entry['answers'].items():
            print(f"{key}: {value}")

        user_answer = input("What is your answer? ")
        user_answer = user_answer.upper()
        if user_answer == entry['correct_answer']:
            print("Correct")
        else:
            print("Better luck next time!")




#=======================================================

start_quiz()
run_quiz(quiz_data)



