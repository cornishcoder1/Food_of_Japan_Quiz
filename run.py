questions = {
        "This dish is a speciality in the region of Gunma, typically consisting of pork tenderloin which is breaded and deep fried.": "C",
        "A type of sushi, consisting of pressed rice usually topped with fish.": "B",
        "These boiled dumplings are usually served in a very light broth, filled with ground meat and vegetables.": "B",
        "Katsuobushi shavings (or bonito flakes) are derived from which fish?": "A",
        "What is Japanese Horseradish also known as?": "C",
        "Found all over Japan in street food markets and sushi restaurants, this fried rolled omelette is typically seasoned with salt and dashi.": "A",
        "Which of the Japanese islands is famous for it’s Tarabagani (King Crab)?": "B",
        "Which Japanese fruit is said to be one of the most expensive in the world?": "C",
        "Which variety of beef is identified by it’s fatty, well-marbled texture?": "C",
        "What fish-shaped pancake is traditionally filled with sweetened adzuki beans?": "B",
}












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

def run_quiz():
        print("quiz is running")

start_quiz()
run_quiz()