Use consistent and effective markdown formatting that is well-structured, easy to follow, and has few grammatical errors when writing a README file.

Write a README.md file in English for the Python application that explains its purpose and the value that it provides to its users.


# Food of Japan Quiz

<p>My command line application built with Python is a quiz titled 'Food of Japan'. Users test their knowledge of Japanese cuisine by answering 10 food themed multiple choice questions, with their score being returned to them at the end of the quiz. They then have the option to play again, or end the quiz. </p>

<a href="https://food-of-japan-quiz.herokuapp.com/" aria-label="Link to open deployed site">Link to deployed site</a>

<img src="assets/images/am_i_responsive_screenshot.png">

------

# Table of Contents:

1. [Flowchart](#flowchart)

2. [Wireframes](#wireframes)

3. [User Experience/Stories](#user-experience)

4. [Features](#features)

5. [Invalid Data Handling](#invalid-data-handling)

6. [Data Model](#data-model)

7. [Testing](#testing)

8. [Bugs](#bugs) \

9. [Other Resources Used](#other-resources-used)

10. [Deployment](#deployment)

11. [Credits](#credits)
   
   
------

# Flowchart
 
I used <a href="https://www.lucid.app">Lucid</a> to create a simple flowchart of the expected flow of logic through the programme from start to finish. This helped me to begin visualising the structure of the code, and what functions may be needed.   

<img src="assets/images/pp3_flowchart.png">


# Wireframe

I produced a basic wireframe with <a href="https://www.balsamiq.com">Balsamiq</a>, as I wanted to include some visual elements at the start of the quiz including a title and some food related images. The wireframe helped me visualise what this could look like when the user initiates the programme. I discovered ASCII images and fonts, which can be used in a command line application, and so implemented this to add some basic styling at the start of the quiz. This wireframe was created during the early planning stages and does not represent the final presentation. 

<img src="assets/images/pp3_wireframe.png">

------

# User Experience 
Present a clear rationale for the development of the project in the README, demonstrating that it has a clear, well-defined purpose addressing the critical goals of the application for a particular target audience (or multiple related audiences).

## Project Goals
- Provide the user with a fun, engaging and easy to play multiple choice quiz.
- Provide some visuals with the use of images and colour to contribute to a positive user experience.
- Provide an appropriate response to all user inputs and ensure any invalid data is handled appropriately. 
- Accurately keep track of and display the user’s score clearly at the end of the quiz. 


## User Stories
As a user I want:
- To play a fun and easy to use quiz.
-  Clear instructions on how to use the quiz.
- To test my knowledge of Japanese cuisine.
- To be informed when my input is invalid, and to be given the opportunity to correct any invalid input without interrupting the flow of the quiz.
- To be able to read the application output clearly. 
- To see my total score out of ten at the end of the quiz.
- To be able to easily repeat the quiz if I want to try again. 

------

# Features 
Document the rationale as to why a particular library/libraries are necessary for the implementation of the project.
Demonstrate, through screenshots, what the project outcomes are and how they have been met.

## Main page and welcome screen 
*Project Goal - Provide some visuals with the use of images and colour to contribute to a positive user experience.*

As design and layout features in command line applications are restrictive, I decided to add a background image to the main page by manipulating the provided template's CSS. I also changed the color of the 'Run Program' button to better match the color scheme. Although not explicitly required for this project, I wanted to enhance the user experience with the addition of some color and visuals. The background image is bright and cheerful, and the Japanese cat salt and pepper shakers are in keeping with the Japanese food theme.

I used ASCII font <a href="https://patorjk.com/software/taag/#p=display&f=Crawford2&t=Food%20of%20Japan!">'Crawford 2'</a> and <a href="https://asciiart.website/index.php?art=food%20and%20drink/other">art by Daniel Au</a> to create the quiz title and sushi icons, and have used the Python module 'Colorama' throughout the program to add color within the terminal.  

The first input in the program asks the user to enter their name. This gives some personalisation to the quiz, as the program returns the name as a welcome, and at the end when the final score is displayed. 


<img src="assets/screenshots/home_screen.png">

## Instructions
*As a user I want clear instructions on how to use the quiz*

Once the user has entered their name, they are given a personalised welcome message, and are presented with a short descripion and simple instructions for the quiz. I have used new line characters to space out the text lines here to improve readability. 

<img src="assets/screenshots/instructions.png">

The user is then asked if they are ready to play the quiz by typing 'y' for yes or 'n' for no. This allows user initiation and control of the logic flow in this stage of the program. If the user types 'y' the quiz will begin, if 'n' is typed then a message appears asking them to type 'y' when ready, and the question repeats.

<img src="assets/screenshots/start_quiz_not_ready.png">

## Questions
*Project Goal - Provide the user with a fun, engaging and easy to play multiple choice quiz.*

*As a user I want to test my knowledge of Japanese cuisine.*

*As a user I want to be able to read the application output clearly.*

The quiz contains 10 multiple choice questions of varying difficulty (depending on the users level of interest and knowledge!), which are interated through in the same order each time the program is run. Each correctly answered question scores 1 point, and if the question is answered incorrectly then 0 points are awarded. To improve readability I have coloured the questions Magenta, and used the 'style.bright' Colorama feature to add boldness to the text. I have also used the tab character to indent the answer choices for the same purpose.  

<img src="assets/screenshots/question.png">

If the correct answer is selected by the user, they are informed with the output 'correct' which is colored in green, followed by the next question. If an incorrect answer is selected, the output 'Oops! Better luck next time' is shown in red. 

<img src="assets/screenshots/question_correct.png">

<img src="assets/screenshots/question_incorrect.png">

## Final Score and Play Again
*Project Goal - Accurately keep track of and display the user’s score clearly at the end of the quiz.*

*As a user I want to see my total score out of ten at the end of the quiz.*

*As a user I want to be able to easily repeat the quiz if I want to try again.*

Once all 10 questions have been iterated through, the user is then presented with their final score. Different messages are displayed, depending on whether the score is equal to or less that 5, or greater than 5. The message is personalised with the users name. 

<img src="assets/screenshots/final_score.png">
<br> 
<img src="assets/screenshots/final_score_2.png">

The user is also asked if they would like to play again, by typing 'y' for yes or 'n' for no. If 'y' is typed the program sequence starts again. If 'n' is typed, a message informs the user the the quiz has ended and to click the 'Run Program' button if they wish to reset the quiz. 

<img src= "assets/screenshots/play_again_end_quiz.png">

# Invalid data handling
Write code that handles empty or invalid input data.
Implement exception/error handling to optimise the user experience

## Upper or lower case characters 
All input will be accepted in lower or upper case. For example if the user selects answer 'a' with an uppercase 'A', this input will still be accepted by the programme as valid. 

## Name Input
Users must enter a string of text in the name input before they can proceed. If the input is left blank, or contains just whitespace, then an error message is displayed and the input is requested again. 

<img src = "assets/screenshots/enter_name_error_handling.png">

## Start Quiz
Users must type 'y' or 'n' to indicate if they are ready to start the quiz. If they enter any other character, then an error message is displayed and the input is requested again. 

<img src = "assets/screenshots/start_quiz_error_handling.png">

## Answer Input 
Users must type 'a', 'b' or 'c' to select their chosen answer. If they enter any other character, then an error message is displayed and the question will be repeated. An invalid answer like this does not effect the users end score. 

<img src="assets/screenshots/answer_input_error_handling.png">

## Play Again 
Users must type 'y' or 'n' to indicate whether or not they wish to play again. If they enter any other character, then an error message is displayed and the input is requested again.

<img src="assets/screenshots/play_again_error_handling.png">


## Features left to implement

I would like to expand the size of the quiz, perhaps by adding an option to select a difficulty level at the beginning. This would then open a specific set of questions for that level. Another nice feature would be to have a high scores board displayed at the end of the quiz, so that the user can see how they did against others. This could be implemented with the help of Google Sheets to push and pull score data. 

------

# Data Model

I used a dictionary in this programme to store the question and answer data for the quiz. I have written the code in a way that means additional questions can be added to the dictionary in the future, without having to amend any other code. This has been achieved through the use of f-Strings in print statements, so that accurate data is always displayed for the user score and total number of questions, regardless of the total number of questions present in the dictionary. 

------

# Testing

## Manual Testing
I have carried out the following manual tests throughout the development process: 
- Given invalid input at each input stage to check invalid data is dealt with in the way I expected.
- Checked f-Strings to ensure that output data is updated automatically and remains accurate, if questions are added to the dictionary. 
- Tested in my local terminal and the deployed Heroku terminal. 
- Submitted my code for peer review. 
- Asked friends and family to play the quiz to check that it works on various browsers, and that the quiz functionality is understandable. 

## Validator Testing

I ran my code through the <a href="http://pep8online.com">PEP8 linter</a>, no problems were detected. 

<img href="assets/screenhots/pep8_validator_screenshot.png">

## Accessibility Testing

Lighthouse scored the site highly on Performance and Accessibility.

<img href="assets/screenshots/lighthouse_validator_screenshot.png">

------

# Bugs
Document validation error-based fixes implemented and identify and explain any unsolved validation errors.

## Fixed

- When I first ran the code through the PEP8 linter, it informed me that some of the code lines in the dictionary were too long. This was also causing some individual words to break in the middle and displaying incorrectly in the terminal. I fixed this by inserting a back slash at the line length limit point and putting all characters after the back slash on to a new line. I had to position the new line carefully so that the questions would still display in the terminal without additional whitespace.
- As a result of peer review, it was pointed out to me that it was possible to still get away with not entering any data in the name input, by hitting space two or more times. To rectify this I used the .strip() method to remove any leading whitespace.  
- During final tests I realised that if I were to add any more questions to the dictionary, the total number of questions in the final score print statements would not update. For example if I added an eleventh question to the dictionary, and the user got all questions right, then the output would display "Your final score is 11 out of 10". This was recified easily as I already had a variable to represent the number of questions in the dictionary, and so inserted this variable into an f_string in the relevant print statements. 

## Unfixed

- No remaining bugs. 

------

# Other resources used

<a href="http://ami.responsivedesign.is/#"> - Am I Responsive</a>

<a href="https://balsamiq.com"> - Balsamiq</a>

<a href="https://developer.chrome.com/docs/devtools/"> - Chrome Dev Tools</a>

<a href="https://www.geeksforgeeks.org/print-colors-python-terminal/"> - Colorama (Python module)</a>

<a href="https://www.lucid.app"> - Lucid</a>

<a href="https://patorjk.com/software/taag/#p=display&f=Crawford2&t=Food%20of%20Japan!"> - Patorjk.com (text to ASCII generator)

------

# Deployment 

Deployment was done at the start of the project to allow device testing throughout the development process. 

My <a href="https://food-of-japan-quiz.herokuapp.com/" aria-label="Link to open deployed site">project</a> was deployed via <a href="https://heroku.com">Heroku</a> as follows:

1. Remove un-used imports from run.py file
2. In order for input methods to work properly in the deployed mock terminal, add a new line character at the end of the text, inside the input method. 
3. If required, create list of requirements with the following command in the terminal:  pip3 freeze > requirements.txt
4. In Heroku account, go to Dashboard and click ‘Create New App’. Give the app a unique name and select region (Europe).
5. Click ‘Create App’.
6. Got to Settings tap and set up Config Vars (not required if not using a creds.json file).
7. Click ‘Add Buildpack’, select Python and click ‘Save Changes’.
8. Then select ‘NodeJS’ and click save again. IMPORTANT - Buildpacks should be in order. Python on top of NodeJS.
9. Click on ‘Deploy’ tab.
10. Select ‘GitHub' as deployment method. 
11. Search for repo name and connect.
12. Click ‘Enable Automatic Deploys’.
13. Ensure that ‘main’ branch is selected in Manual deploy section and click ‘Deploy Branch’.
14. Once deployed, click ‘view’ to access deployed project.  

------

# Credits 

## Content

I used the following websites for research: 

- The videos of YouTubers <a href="https://www.youtube.com/c/AbroadinJapan">Chris Broad</a> and <a href="https://www.youtube.com/c/IWillAlwaysTravelforFood">I Will Always Always Travel For Food</a>, for quiz question inspiration:  
    - <a href="https://www.youtube.com/watch?v=3n_rgmagVoE"> What $250 Buys You at a Japanese Hot Spring Inn</a>
    - <a href="https://www.youtube.com/watch?v=2j2TO_QSxUo"> 5 Must Try Dishes in Hokkaido</a>
    - <a href="https://www.youtube.com/watch?v=IMSYyb5U-9g"> What $20 Buys You at a Japanese Street Food Market</a>
    - <a href="https://www.youtube.com/watch?v=MWOwEWMquP8"> I Tried Kobe Beef for the First Time</a>
    - <a href="https://www.youtube.com/watch?v=RsuuFrEPLrE">Japanese Street Food in TSUKIJI Market</a>

<br>

## Media 

1. Background image from <a href="https://www.8wallpapers.com/5072.html">8wallpapers.com</a> 

2. Sushi ASCII by Daniel Au, from <a href="https://asciiart.website/">Ascii Art</a>

<br>

## Acknowledgements 

- Declan_5P_Lead and Sean Young for helping me with my understanding of while loops.
- Dave_Horrocks_5p_lead for his extensive peer review, and for drawing my attention to the name input bug. 
- Johann from Tutor Support for helping me with my dictionary. 
- Computer Science Tutorials' YouTube Video <a href="https://www.youtube.com/watch?v=LXSvzUimHBk"> 'Simple Quiz Plus Flowchart Python' for helping me get started with a flowchart.</a>
- Bro Code's YouTube video <a href="https://www.youtube.com/watch?v=yriw5Zh406s"> 'Python Quiz game'</a> for giving me an initial guide on how to structure code for a python quiz. 
- The Grimes Teacher's YouTube video <a href="https://www.youtube.com/watch?v=arcFqEuV_XQ"> 'Python: Print ASCII Art'</a> for showing me how to do just that. 
- The Geeks for Geeks article <a href="https://www.geeksforgeeks.org/print-colors-python-terminal/"> 'Print Colors To Python Terminal'</a> for showing me how to use Colorama. 
- The DelftStack article <a href="https://www.delftstack.com/howto/python/number-of-keys-in-dictionary-python/"> 'Count Number of Dictionary Keys Python'</a> for introducing the enumerate() function to me.
- Love Running project for reference and guidance. 
- Victor Miclovich (Mentor)
- <a href="http://w3schools.com"> W3 Schools</a> for tips on media queries, date inputs on forms and centering tables. 

 