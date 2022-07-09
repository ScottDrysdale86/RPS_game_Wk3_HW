from random import randint
from models.player import Player


class Game:
    # set up game template
    def __init__(self, _player_1, _player_2):
        self.player_1 = _player_1
        self.player_2 = _player_2

    # take 2 strings from address bar and return winner
    def basic_play(player1_choice, player2_choice):
        while player1_choice != player2_choice:
            if player1_choice == "rock" and player2_choice == "scissors":
                return f"Player 1 wins"
            elif player1_choice == "paper" and player2_choice == "rock":
                return f"Player 1 wins"
            elif player1_choice == "scissors" and player2_choice == "paper":
                return f"Player 1 wins"
            else:
                return f"Player 2 wins"
        return f"It is a draw"

    # get random computer choice, take 1 string from the address bar and return winner
    def basic_play_computer(player_choice):
        # get compyer choice
        computer = randint(1, 3)
        if computer == 1:
            computer_choice = "rock"
        elif computer == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"
        # decide on winner
        while player_choice != computer_choice:
            if player_choice == "rock" and computer_choice == "scissors":
                return f"Player 1 wins. Computer chose {computer_choice}"
            elif player_choice == "paper" and computer_choice == "rock":
                return f"Player 1 wins. Computer chose {computer_choice}"
            elif player_choice == "scissors" and computer_choice == "paper":
                return f"Player 1 wins. Computer chose {computer_choice}"
            else:
                return f"Computer wins. Computer chose {computer_choice}"
        return f"It is a draw"

    # find random computer choice and return string
    def computer_choice():
        computer_rand = randint(1, 3)
        if computer_rand == 1:
            return "rock"
        elif computer_rand == 2:
            return "paper"
        else:
            return "scissors"

    # take in 2 player objects and return the winning object
    def play_computer(player_1, player_2):
        while player_1.choice.lower() != player_2.choice.lower():
            if (
                player_1.choice.lower() == "rock"
                and player_2.choice.lower() == "scissors"
            ):
                return player_1
            elif (
                player_1.choice.lower() == "paper" and player_2.choice.lower() == "rock"
            ):
                return player_1
            elif (
                player_1.choice.lower() == "scissors"
                and player_2.choice.lower() == "paper"
            ):
                return player_1
            else:
                return player_2
        return None
