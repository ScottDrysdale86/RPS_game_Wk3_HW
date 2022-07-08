from platform import java_ver
from app import app
from flask import render_template, request, redirect
from models.game import Game


@app.route("/")
def welcome():
    return render_template("index.html", title="Rock, Paper, Scissors Game")


@app.route("/<p1_choice>/<p2_choice>")
def basic(p1_choice, p2_choice):
    return render_template(
        "basic.html",
        p1_choice=p1_choice,
        p2_choice=p2_choice,
        title="Rock Paper Scissors Game",
        result=Game.play(p1_choice, p2_choice),
    )


@app.route("/computer/<p_choice>")
def computer(p_choice):
    return render_template(
        "computer.html",
        p_choice=p_choice,
        title="Rock, Paper, Scissors Game",
        result=Game.play_computer(p_choice),
    )


@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        player_name = request.form.get("p1-name")
        player_choice = request.form.get("p1-choice")
        return Game.play_computer(player_choice)
    return render_template(
        "play.html",
        title="Rock, Paper, Scissors Game",
    )
