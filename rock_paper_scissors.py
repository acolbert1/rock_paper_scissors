import random
# Rock Paper Scissors Game

#     Create a rock-paper-scissors game.
#     Ask the player to pick rock, paper or scissors.
#     Have the computer chose its move.
#     Compare the choices and decide who wins.
#     Print the results.
#     Subgoals:
#         Give the player the option to play again.
#         Keep a record of the score (e.g. Player: 3 / Computer: 6).


#1. take input from the user
#2. parse the input - if its rock, paper, or scissors
#3. have the computer do a random choice of the 3
#4. if computer input is equal to a certain response then return 

random_response = ["Rock", "Scissors", "Paper"]

def game():
    user_input = input("Whats your input: ")
    computer = random.choice(random_response)
    #player chooses Scissors
    if user_input == "Scissors" and computer == "Rock":
        print("Player loses! Rock beats Scissors!")
    elif user_input == "Scissors" and computer == "Paper":
        print("Player wins! Scissors beats paper!")
    #player chooses Paper
    if user_input == "Paper" and computer == "Rock":
        print("Player wins! Paper beats Rock!")
    elif user_input == "Paper" and computer == "Scissors":
        print("Player loses! Scissors beats Paper!")
    #player chooses Rock
    if user_input == "Rock" and computer == "Scissors":
        print("Player wins! Rock beats Scissors!")
    elif user_input == "Rock" and computer == "Paper":
        print("Player loses! Paper beats Rock!")

    if user_input == computer:
        print("The result is a tie!")


game()
