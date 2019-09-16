import random

class Game:
    
    def __init__(self):
        self.player_total = 0
        self.computer_total = 0

    def another_round(self):
        play_again = input("Would you like to play again? ")
        if play_again == "y" or play_again == "yes":
            self.play()

        if play_again == "n" or play_again == "no":
            print("Thanks for playing! Until next time. The final score was Computer Score: " + str(self.computer_total) + " and Player score: " + str(self.player_total))
        elif play_again != "n" and play_again != "no" and play_again != "yes" and play_again != "y":
            print("That isn't a yes or a no. Please try again")
            self.another_round()
        
    def current_score(self):
        print("The current Computer score is: " + str(self.computer_total) + " and the current Player score is: " + str(self.player_total))
        self.another_round()
    
    def play(self):
        rock = "rock"
        paper = "paper"
        scissors = "scissors"
        random_response = [rock, paper, scissors]

        user_input = input("Let's play a game of Rock, Paper, Scissors. Throw out your guess: ").lower()
        computer = random.choice(random_response)
    
        if user_input != scissors and user_input != paper and user_input != rock:
            print("That isn't a proper input. Please try again")
            self.play()
 
        if user_input == scissors and computer == rock:
            print("Player loses! Rock beats Scissors!")
            self.computer_total = self.computer_total + 1
            self.current_score()
            
        elif user_input == scissors and computer == paper:  
            print("Player wins! Scissors beats paper!")
            self.player_total = self.player_total + 1
            self.current_score()
            
        if user_input == paper and computer == rock:
            print("Player wins! Paper beats Rock!")
            self.player_total = self.player_total + 1
            self.current_score()

        elif user_input == paper and computer == scissors:
            print("Player loses! Scissors beats Paper!")
            self.computer_total = self.computer_total + 1
            self.current_score()
        
        if user_input == rock and computer == scissors:
            print("Player wins! Rock beats Scissors!")
            self.player_total = self.player_total + 1
            self.current_score()
            
        elif user_input == rock and computer == paper:
            print("Player loses! Paper beats Rock!")
            self.computer_total = self.computer_total + 1
            self.current_score()

        if user_input == computer:
            print("The result is a tie!")
            self.current_score()

game = Game()
game.play()
