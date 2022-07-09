from app import app
from flask import render_template, request, redirect
from models.game import Game
from models.player import Player


@app.route("/")
def welcome():
    return render_template("index.html", title="Rock, Paper, Scissors Game")


# 2 player in address bar
@app.route("/<p1_choice>/<p2_choice>")
def basic(p1_choice, p2_choice):
    return render_template(
        "basic.html",
        p1_choice=p1_choice,
        p2_choice=p2_choice,
        title="Rock Paper Scissors Game",
        result=Game.basic_play(p1_choice, p2_choice),
    )


# vs computer in address bar
@app.route("/computer/<p_choice>")
def computer(p_choice):
    return render_template(
        "basic_computer.html",
        p_choice=p_choice,
        title="Rock, Paper, Scissors Game",
        result=Game.basic_play_computer(p_choice),
    )


# vs computer using form input
@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        player_name = request.form.get("p1-name")
        player_choice = request.form.get("p1-choice")
        player_1 = Player(player_name, player_choice)
        computer_choice = Game.computer_choice()
        computer = Player("Computer", computer_choice)
        result = Game.play_computer(player_1, computer)
        if result != None:
            result_name = result.name
        else:
            result_name = "No-one"
        return render_template(
            "winner.html",
            result_name=result_name,
            player_name=player_name,
            player_choice=player_choice,
            computer_name="computer",
            computer_choice=computer_choice,
        )
    return render_template("v_computer.html", title="Rock, Paper, Scissors Game")


# 2 PLayer using form input
@app.route("/2player", methods=["GET", "POST"])
def two_play():
    if request.method == "POST":
        player1_name = request.form.get("p1-name")
        player1_choice = request.form.get("p1-choice")
        player_1 = Player(player1_name, player1_choice)

        player2_name = request.form.get("p2-name")
        player2_choice = request.form.get("p2-choice")
        player_2 = Player(player2_name, player2_choice)

        result = Game.play_computer(player_1, player_2)
        if result != None:
            result_name = result.name
        else:
            result_name = "No-one"
        return render_template(
            "winner_2play.html",
            result_name=result_name,
            player1_name=player1_name,
            player1_choice=player1_choice,
            player2_name=player2_name,
            player2_choice=player2_choice,
        )
    return render_template("2player.html", title="Rock, Paper, Scissors Game")
