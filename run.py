def start_quiz():
    """
    Starting point of quiz, displays ASCII title text and sushi images. Gets user name and starts quiz.
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
            '.________.'           '.__|;;|__.'           '.________.'

    \n""")

    #global name 
    name = input("Please enter you name:\n")
    while name == "" or name == " ":
        print("Please enter your name to begin the quiz")
        name = input("Please enter you name:\n")
        break
    else:
        print(f"Welcome to Food of Japan {name}!\n")
        print("Take the quiz to test your knowledge of Japanese cuisine.\n")
        print("There are 10 multiple choice questions, good luck!\n")


start_quiz()