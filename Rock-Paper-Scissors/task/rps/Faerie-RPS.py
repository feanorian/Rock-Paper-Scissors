
#This is a Rock-Paper-Scissors game I did for Jetbrains Academy, but with a twist. There are
#2 modes, regular rock-paper-scissors, and a mode where a used can input as many options as
#they choose. There are a few print statements that are greyed out. If you would like to see
#the output of the algorithm or the running score,  you may remove the '#'
#I will not explain the more complicated functions, because I would like people who are getting
#into coding to try to figure it out on their own. It's a little tricky, but not impossible
#Additionally, I could get all of this to run in a single function instead of 2. I will save that
#for the next revision, as I only wanted to get this to work, and elegance was not the priority.

import random
#This bit of code opens the file where the scores can be read from (it doesn't store scores
#yet, but that will come in the next revision. It then splits that input and stores it
# in an array called split_score_array
my_file = open('rating.txt', 'r+')
score_array = my_file.readlines()
split_score_array = []
#choices array stores the choices fore regular rock-paper-scissors
choices = ["rock", "paper", "scissors"]
#win_array stores the values that can be beaten by the choice of the user
win_array = []

#this function reads the player score as a string and returns an integer value of the score
# read from rating.txt
def get_score(score_array):

    my_score = []
    for entry in score_array:
        my_score_array = entry.split()
        split_score_array.append(my_score_array)

    for scores in split_score_array:

        if scores[0] == name:
            score_string = scores
            my_score = score_string
            score_int = int(my_score[1])

        elif scores[0] != name:
            my_score.append(name)
            my_score.append('0')
            score_int = int(my_score[1])

    return score_int

#the logic of basic rock-paper-scissors
def rock_paper_scissors():
    score_int = get_score(score_array)

    while True:

        index = random.randint(0, 2)
        computer_choice = choices[index]
        player_choice = input()

        if ((player_choice == "rock") and (computer_choice == "paper")) or (
                (player_choice == "paper") and (computer_choice == "scissors")) or (
                (player_choice == "scissors") and (computer_choice == "rock")):
            print("Sorry, but the computer chose %s" % computer_choice)
            print('Your rating: %s' % score_int)

        elif ((player_choice == "paper") and (computer_choice == "rock")) or (
                (player_choice == "scissors") and (computer_choice == "paper")) or (
                (player_choice == "rock") and (computer_choice == "scissors")):
            print("Well done. The computer chose %s and failed" % computer_choice)
            score_int += 100
            print(score_int)

        elif computer_choice == player_choice:
            print("There is a draw (%s)" % computer_choice)
            score_int += 50
            print('Your rating: %s' % score_int)

        elif player_choice == "!rating":
            print('Your rating: %s' % score_int)

        elif player_choice == "!exit":
            print("Bye!")
            my_file.close()
            exit()

        else:
            print("Invalid input")
#the function of advanced rock-paper-scissors that I call faerie-rps
def faerie_rps(options):
    score_int = get_score(score_array)
    while True:
        choice = options.split(',')
        index = random.randint(0, len(choice)-1)
        losing_array = []
        computer_choice = choice[index]
        player_choice = input()


        if player_choice == '!rating':
            print("Your rating: %s" % score_int)
        elif player_choice == '!exit':
            exit()


        elif player_choice in choice:
            player_index = choice.index(player_choice)
            if player_index <= len(choice):
                win_array = choice[0:player_index]

            for element in choice:
                if element not in win_array and element != player_choice:
                    losing_array.append(element)
            while len(win_array) != len(losing_array):
                if len(win_array) < len(losing_array):
                    win_array.append(losing_array[-1])
                    losing_array.remove(losing_array[-1])
                elif len(win_array) > len(losing_array):
                    losing_array.append(win_array[0])
                    win_array.remove(win_array[0])


            if player_choice == computer_choice:
                print("There is a draw (%s)" % player_choice)
                score_int += 50
                #print('Your rating: %s' % score_int)
            elif computer_choice in win_array:
                print("Well done, computer chose %s and failed" % computer_choice)
                score_int += 100
                #print('Your rating: %s' % score_int)
            elif computer_choice in losing_array:
                print("Sorry, but the computer chose %s " % computer_choice)
                #print('Your rating: %s' % score_int)
        else:
            print('Invalid input')
        #print(win_array)
        #print(losing_array)
        #print(computer_choice)
#Reads user input and options. if options is empty, you get to play standard rock-paper-scissors
#if the user inputs options, then you go to faerie-rps
name = input("Enter your name:   ")
print("Hello, " + name)
options = input("Please enter your options:  ")
print('Okay, let\'s start')
if len(options) == 0:
    rock_paper_scissors()
else:
    faerie_rps(options)


