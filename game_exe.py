import random
from questions import *


# function to generate the 4 answer strings in random order with correct answer as return value
def get_answers(answer_tuple):
    which_answer = [0, 1, 2, 3]                                             # list of 0, 1, 2, 3 to later chose answer
    random.shuffle(which_answer)                                            # randomly shuffled list from above
    answer_letter = ("A", "B", "C", "D")                                    # tuple with letters to number the answers
    for i in range(4):
        i_answer = which_answer.pop()                                       # number of the current answer, random
        if (i_answer == 0):
            correct_answer_letter = answer_letter[i].lower()                # save the letter (its lowercase) when answer 0 (the correct one) is chosen
        print(f"   ({answer_letter[i]})\t{answer_tuple[i_answer]}")         # print the 4 answer possibilities
    return correct_answer_letter


# enter name and score to the leaderboard
def add_leaderboard_entry(player_name, score):
    return


# prints out leaderboard
def get_leaderboard():
    return


# processing questions for use in program
questions_dick = kt_questions                                               # chosing the question set
questions_list = list(questions_dick.items())                               # adding the questions + their answers to a list and shuffling it for randomization
random.shuffle(questions_list)
n_questions = len(questions_dick)                                           # number of available questions


# +++ program start +++

# introduction to the program
print("Please enter your name: ")
player_name = input()
print(f"\nWelcome to Kern- / Teilchenphysik, {player_name}, I want to play a game with you. We have a total of {n_questions} questions to answer for you!\n\n")

# iterating through all question until an error is made
i_questions = 0
while (i_questions < n_questions):
    # ask question and ask for answer
    questions_list_entry = questions_list.pop()
    print(f"Question ({i_questions+1}/{n_questions}): {questions_list_entry[0]}")
    correct_answer_letter = get_answers(questions_list_entry[1])
    print("\nPlease enter your answer ('a', 'b', 'c', 'd') or quit ('q'):")

    # enter answer
    command = input()
    if command == '-q' or command == 'quit' or command == 'q':
        print(f"\n +++ You are a quitter, you scored {i_questions} out of {n_questions}. +++ \n")
        break
    elif command == correct_answer_letter:
        print(f"\n +++ CORRECT! You are at {i_questions+1} out of {n_questions}. +++ \n")
    else:
        print(f"\n +++ FALSE! You are a loser, you scored {i_questions} out of {n_questions}. +++ \n")
        break

    # initiate next iteration step
    i_questions += 1