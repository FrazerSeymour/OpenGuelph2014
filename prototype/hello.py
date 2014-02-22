from flask import Flask, render_template
from pickle import load
from random import randint
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name=None):
    return render_template('main.html', message = messages[randint(0, 3)], name = name)

if __name__ == '__main__':
    f = open("messages.pickle")
    messages = load(f)
    f.close()

    app.run()
