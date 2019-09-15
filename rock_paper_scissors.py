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

rock = "rock"
paper = "paper"
scissors = "scissors"
random_response = [rock, paper, scissors]

def game():
    user_input = input("Whats your input: ").lower()
    computer = random.choice(random_response)
    #player chooses Scissors
    if user_input == scissors and computer == rock:
        print("Player loses! Rock beats Scissors!")
    elif user_input == scissors and computer == paper:
        print("Player wins! Scissors beats paper!")
    #player chooses Paper
    if user_input == paper and computer == rock:
        print("Player wins! Paper beats Rock!")
    elif user_input == paper and computer == scissors:
        print("Player loses! Scissors beats Paper!")
    #player chooses Rock
    if user_input == rock and computer == scissors:
        print("Player wins! Rock beats Scissors!")
    elif user_input == rock and computer == paper:
        print("Player loses! Paper beats Rock!")

    if user_input == computer:
        print("The result is a tie!")


game()

