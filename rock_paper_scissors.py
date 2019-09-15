import random

rock = "rock"
paper = "paper"
scissors = "scissors"
random_response = [rock, paper, scissors]

def another_round():
    play_again = input("Would you like to play again? ")
    if play_again == "y" or play_again == "yes":
        return game()

    if play_again == "n" or play_again == "no":
        print("Thanks for playing! Until next time. The final score was Computer Score: " + str(computer_total) + " and Player score: " + str(player_total))
    elif play_again != "n" or play_again != "no" or play_again != "yes" or play_again != "y":
        print("That isn't a yes or a no. Please try again")
        
        return another_round()
        

def current_score():
    print("The current Computer score is: " + str(computer_total) + " and the current Player score is: " + str(player_total))

player_total = 0
computer_total = 0


def game():
    user_input = input("Let's play a game of Rock, Paper, Scissors. Throw out your guess: ").lower()
    computer = random.choice(random_response)
    global computer_total, player_total

    if user_input != "scissors" or user_input != "pape" or user_input != "rock":
        print("That isn't a proper input. Please try again")
 
    
    if user_input == scissors and computer == rock:
        print("Player loses! Rock beats Scissors!")
        computer_total = computer_total + 1
        current_score()
        
    elif user_input == scissors and computer == paper:  
        print("Player wins! Scissors beats paper!")
        player_total = player_total + 1
        current_score()
        
    if user_input == paper and computer == rock:
        print("Player wins! Paper beats Rock!")
        player_total = player_total + 1
        current_score()

    elif user_input == paper and computer == scissors:
        print("Player loses! Scissors beats Paper!")
        computer_total = computer_total + 1
        current_score()
    
    if user_input == rock and computer == scissors:
        print("Player wins! Rock beats Scissors!")
        player_total = player_total + 1
        current_score()
        
    elif user_input == rock and computer == paper:
        print("Player loses! Paper beats Rock!")
        computer_total = computer_total + 1
        current_score()

    if user_input == computer:
        print("The result is a tie!")
        current_score()

    another_round()

game()
