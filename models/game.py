from random import randint


class Game:
    def play(player1_choice, player2_choice):
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

    def play_computer(player_choice):
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
