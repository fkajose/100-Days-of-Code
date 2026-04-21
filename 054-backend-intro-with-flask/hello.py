from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text = func()
        return f'<b>{text}</b>'
    return wrapper


def make_italic(func):
    def wrapper():
        text = func()
        return f'<em>{text}</em>'
    return wrapper


def make_underlined(func):
    def wrapper():
        text = func()
        return f'<u>{text}</u>'
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>\
        <p>This is a paragraph</p>\
            <img src="https://media.giphy.com/media/n5CHDD8c4sW18Dqz3z/giphy.gif" width=300>'


hello_world


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def say_bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)
