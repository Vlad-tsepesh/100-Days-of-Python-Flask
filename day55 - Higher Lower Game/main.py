from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return ('Hello, World')

@app.route('/name/<name>')
def hello_name(name):
    return f"{name + 12}hai"

if __name__=="__main__":
    app.run(debug=True)
