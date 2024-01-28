from boggle import Boggle
from flask import Flask, jsonify, session, render_template, request, redirect

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "some_key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def setup_game():
    # adding a brand new board to session via cookies
    session['board'] = boggle_game.make_board()
    session['score'] = 0
    session['highscore'] = 0
    nplays = session.get("nplays", 0)
    return redirect("/board")

@app.route("/board")
def display_board():
    """Returns gameboard"""
    nplays = session.get("nplays", 0)
    session['nplays'] = nplays + 1
    return render_template("game_board.html")

@app.route("/check-word")
def check_word():
    """return the validity of the input word"""
    word = request.args["word"]
    result = boggle_game.check_valid_word(session['board'], word)
    return jsonify({"result": result})

@app.route("/get-score")
def get_score():
    """handles highscore and returns a score to display"""
    addingAmount = int(request.args["addingAmount"])
    score = session["score"]
    score += addingAmount
    session["score"] = score

    highscore = session.get("highscore", 0)
    if (score > highscore):
        highscore = score
        session["highscore"] = highscore
    return jsonify({"score": session["score"]})