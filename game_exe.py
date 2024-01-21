import random
import numpy as np
from questions import *
from comments import *


# covered topics
question_sets = {
    "Kern- / Teilchenphysik": kt_questions, 
    "Festkörperphysik": fk_questions,
}


# gets the key of the selected questions set
def get_question_set(question_sets):
    list_of_question_sets = list(question_sets)
    for i, question_set in enumerate(list_of_question_sets):
        print(f"   ({i})\t{question_set}")
    n_question_set = int(input())
    return list_of_question_sets[n_question_set]


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
def add_leaderboard_entry(player_name, score, question_set):
    with open("leaderboard.txt", "a") as leaderboard:
        leaderboard.write(f"{score[0]},{player_name} ({score[0]}/{score[1]} {question_set})\n")
    return


# prints out leaderboard
def print_leaderboard():
    leaderboard = np.loadtxt('./leaderboard.txt', delimiter = ',', dtype = str)
    dick_of_leaders = {}
    # add players to the dictionary of leaders
    if (leaderboard.ndim == 1):                                             # only one entry / leaderboard array has only one dimension
        dick_of_leaders[int(leaderboard[0])] = leaderboard[1]
    else:                                                                   # leaderboard array has more than 1 entry
        for entry in leaderboard:
            key_number = int(entry[0])
            if key_number in dick_of_leaders.keys():                        # append player to his score entry
                dick_of_leaders[key_number] = dick_of_leaders[key_number] + ',\n\t' +  entry[1]
            else:                                                           # add a players score entry
                dick_of_leaders[key_number] = entry[1]
    # handle and print out the dictionary
    dick_of_leaders_reverse_sorted = dict(reversed(sorted(dick_of_leaders.items())))
    print("Here are the current leaders (number of correct answers, plus names with amount of available questions in brackets):")
    for key, value in dick_of_leaders_reverse_sorted.items():
        print(f"   ({key})\t{value}")
    print()
    return


# +++ program start +++

# entering name and topic
print("Please enter your name: ")
player_name = input()                                                       # chosing name                         

print("\nPlease chose your desired question set:")
question_set = get_question_set(question_sets)                              # chosing the question set

# processing question set for use in program
questions_dick = question_sets[question_set]                                # getting the dictionary from its above returned value
questions_list = list(questions_dick.items())                               # adding the questions + their answers to a list and shuffling it for randomization
random.shuffle(questions_list)
n_questions = len(questions_dick)                                           # number of available questions
print(f"\n +++ Welcome to {question_set}, {player_name}. We have a total of {n_questions} questions to answer for you! +++ \n\n")

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
        print(f"\n +++ RICHTIG! {random.choice(random_stoll)} Du hast {i_questions+1} aus {n_questions} Fragen richtig beantwortet. +++ \n")
    else:
        print(f"\n +++ FALSE! You loser, ({correct_answer_letter.upper()}) was correct. You scored {i_questions} out of {n_questions} questions. +++ \n")
        break
    # initiate next iteration step
    i_questions += 1


# +++ program end +++

# add name to leaderboard and print it out
add_leaderboard_entry(player_name, (i_questions, n_questions), question_set)
print_leaderboard()