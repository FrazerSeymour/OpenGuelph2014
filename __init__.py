from flask import Flask, render_template
from pickle import load
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/go/')
def go():
    return render_template("go.html", places=places)

if __name__ == '__main__':
    f = open("./places.pickle", 'r')
    places = load(f)
    f.close()

    app.run()
