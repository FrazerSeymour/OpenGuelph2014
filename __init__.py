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


@app.route('/do/')
def do():
    return render_template("go.html", places=events)


@app.route('/place/<placeName>/')
def showPlace(placeName = None):
    for place in places:
        if place.getName() == placeName:
            uc_time = getNextTime("University Centre", place.getUcRoute())
            dt_time = getNextTime("Guelph Central Station", place.getDtRoute())
            return render_template("place.html", place=place, dt_time=dt_time, uc_time=uc_time)


@app.route('/dt_path/<placeName>/')
def showDtPath(placeName = None):
    for place in places:
        if place.getName() == placeName:
            time = getNextTime("Guelph Central Station", place.getDtRoute())
            return render_template("dt_path.html", place=place, time=time)


@app.route('/uc_path/<placeName>/')
def showUcPath(placeName = None):
    for place in places:
        if place.getName() == placeName:
            time = getNextTime("University Centre", place.getDtRoute())
            return render_template("uc_path.html", place=place, time=time)


if __name__ == '__main__':
    f = open("./places.pickle", 'r')
    places = load(f)
    f.close()

    f = open("./events.pickle", 'r')
    events = load(f)
    f.close()

    app.run()
