import random
from flask import Flask
app = Flask(__name__)

number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def check_guess(guess):
    if guess == number:
        return '<h1 style="color:Green;">You found me!</h1>\
                <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500>'
    elif guess > number:
        return '<h1 style="color:Purple;">Too high, try again!</h1>\
                <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500>'
    else:
        return '<h1 style="color:Red;">Too low, try again!</h1>\
                <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500>'


if __name__ == '__main__':
    app.run(debug=True)
