import random
from flask import Flask, request, redirect, url_for, render_template

headline = "Guess a number between 0 and 9"
app = Flask(__name__)
number = random.randint(0,9)

def guess_template(function):
    def wrapper(*args, **kwargs):
        text = function(*args, **kwargs)
        return render_template("guess.html", headline=text)
    wrapper.__name__ = function.__name__
    return wrapper

@app.route("/")
def play_game():
    nr = request.args.get('nr')
    if nr is None or nr == "":
        return render_template("guess.html", headline="Guess a number 0-9")
    if int(nr) == number:
        return redirect(url_for('winner'))
    return redirect(url_for('tryagain'))

@app.route("/winner")
def winner():
    return render_template("winner.html", number=number)

@app.route("/tryagain")
@guess_template
def tryagain():
    return "Wrong! Try again!"

if __name__ == "__main__":
    app.run(debug=True)

