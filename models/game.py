from random import randint
from models.player import Player


class Game:
    def __init__(self, _player_1, _player_2):
        self.player_1 = _player_1
        self.player_2 = _player_2

    def basic_play(player1_choice, player2_choice):
        while player1_choice != player2_choice:
            if player1_choice == "rock" and player2_choice == "scissors":
                return f"Player 1 wins by playing rock"
            elif player1_choice == "paper" and player2_choice == "rock":
                return f"Player 1 wins by playing paper"
            elif player1_choice == "scissors" and player2_choice == "paper":
                return f"Player 1 wins by playing scissors"
            else:
                return f"Player 2 wins"
        return f"It is a draw"

    def basic_play_computer(player_choice):
        computer = randint(1, 3)
        if computer == 1:
            computer_choice = "rock"
        elif computer == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

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

    def play(player_1, player_2):
        while player_1.choice.lower() != player_2.choice.lower():
            if player_1.choice.lower() == "rock" and player_2.choice.lower() == "scissors":
                return player_1
            elif player_1.choice.lower() == "paper" and player_2.choice.lower() == "rock":
                return player_1
            elif player_1.choice.lower() == "scissors" and player_2.choice.lower() == "paper":
                return player_1
            else:
                return player_2
        return None

    def computer_choice():
        computer_rand = randint(1, 3)
        if computer_rand == 1:
            return "rock"
        elif computer_rand == 2:
            return "paper"
        else:
            return "scissors"

    def play_computer(player_1, computer):
        while player_1.choice.lower() != computer.choice.lower():
            if player_1.choice.lower() == "rock" and computer.choice.lower() == "scissors":
                return player_1
            elif player_1.choice.lower() == "paper" and computer.choice.lower() == "rock":
                return player_1
            elif player_1.choice.lower() == "scissors" and computer.choice.lower() == "paper":
                return player_1
            else:
                return computer
        return None
