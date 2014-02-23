from flask import Flask, render_template
from openguelph.calculations import *
from pickle import load
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/go/')
def go():
    return render_template("go.html", places=places)

@app.route('/place/<placeName>')
def showPlace(placeName = None):
    for place in places:
        if place.getName() == placeName:
            uc_time = getNextTime("University Centre", place.getUcRoute())
            dt_time = getNextTime("Guelph Central Station", place.getDtRoute())
            return render_template("place.html", place=place, dt_time=dt_time, uc_time=uc_time)

if __name__ == '__main__':
    f = open("./places.pickle", 'r')
    places = load(f)
    f.close()

    app.run()
