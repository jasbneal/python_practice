# 7 March 2021
# Starting Out With Python Programming Exercise 8
# In this programming exercise you will create a simple trivia game for two players.
# The program will work like this:
# Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
# should be a total of 10 questions.) When a question is displayed, 4 possible answers are
# also displayed. Only one of the answers is correct, and if the player selects the correct
# answer, he or she earns a point.
# After answers have been selected for all the questions, the program displays the number
# of points earned by each player and declares the player with the highest number of points
# the winner.

# To create this program, write a Question class to hold the data for a trivia question. The
# Question class should have attributes for the following data:
# a trivia question, possible answer 1, possible answer 2, possible answer 3, possible answer 4,
# the number of correct answer (1, 2, 3, or 4)

# The Question class also should have an appropriate __init__ method, accessors, and mutators. 
# The program should have a list or a dictionary containing 10 Question objects, one for each
# trivia question. Make up your own trivia questions on the subject or subjects of your choice
# for the objects.

import Question_Class
import pickle
import random

def main():
    # Attempts to open the question_bank file or creates a new set of 10 questions and 
    # adds them to the question_dct dictionary.
    try:
        input_file = open('question_bank.dat', 'rb')
        question_dct = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        question_dct = {}
        for i in range(10):
            quest = input("Enter the question you'd like to add to the question bank: ")
            A = input('Enter the first possible answer (Option A): ')
            B = input('Enter the second possible answer (Option B): ')
            C = input('Enter the third possible answer (Option C): ')
            D = input('Enter the fourth possible answer (Option D): ')
            correct_ans = input('Enter whether the correct answer is A, B, C or D: ')
            if correct_ans != 'A' and correct_ans != 'B' and correct_ans != 'C' and correct_ans != 'D':
                correct_ans = input("You've entered an invalid response. Please enter either A, B, C, or D: ")
            obj = Question_Class.Question(quest, A, B, C, D, correct_ans)
            question_dct[i] = obj

    # Creates a list of the question_dct. (This allows the program to randomly choose a number and delete
    # the number from the list when displaying the questions.)
    quest_bank = list(question_dct)

    print('Player 1 will answer 5 trivia questions.')

    # Asks player 1 five questions. Adds +1 to the p1_total if the correct answer is given. Removes
    # the number from the quest_bank list.
    p1_total = 0
    for i in range(5):
        num = random.choice(quest_bank)
        p1_total += answer_question(num, question_dct)
        quest_bank.remove(num)
    
    # Asks player 2 five questions. Adds +1 to the p2_total if the correct answer is given. Removes
    # the number from the quest_bank list.
    print()
    print('Player 2 will answer 5 trivia questions.')
    p2_total = 0
    for i in range(5):
        num = random.choice(quest_bank)
        p2_total += answer_question(num, question_dct)
        quest_bank.remove(num)

    # Displays the total correctly answered questions and determines the winner. 
    print()
    print('Player 1 Correctly Answered Questions:', p1_total)
    print('Player 2 Correctly Answered Questions:', p2_total)

    if p1_total > p2_total:
        print('Player 1 Wins!')
    elif p2_total > p1_total:
        print('Player 2 Wins!')
    else:
        print("It's a tie!")

    output_file = open('question_bank.dat', 'wb')
    pickle.dump(question_dct, output_file)
    output_file.close()

def answer_question(num, dct):
# Using the number given, prints the question and possible answers of the respective
# object. Returns 1 if the correct_ans == response and returns 0 if the correct_ans != response.
    obj = dct[num]
    print(obj)
    response = input('Enter your answer: ')
    while response != 'A' and response != 'B' and response != 'C' and response != 'D':
        print('ERROR: You must enter either A, B, C, or D.')
        response = input('Enter your answer: ')
    if obj.get_correct_ans() == response:
        print('Correct!')
        return 1
    else:
        print("That's incorrect.")
        return 0

main()
