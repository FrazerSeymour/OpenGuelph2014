from math import sqrt
from openguelph.classes import *
from pickle import load

def calculateDistance(x1, y1, x2, y2):
    x = (x1 - x2)
    x = x * x
    y = (y1 - y2)
    y = y * y
    return sqrt(x + y)


if __name__ == "__main__":
    f = open("./resources/parks.pickle", 'r')
    parks = load(f)
    f.close()

    f = open("./resources/stops.pickle", 'r')
    stops = load(f)
    f.close()
    
    user_input = raw_input("Type in the name of a park: ")

    user_park = False
    for park in parks:
        if park.getName() == user_input.upper():
            user_park = park
    
    if user_park != False:
        print user_park.getName(), user_park.getLat(), user_park.getLon()

    distance = 100
    park_lat = float(user_park.getLat())
    park_lon = float(user_park.getLon())
    user_stop = False

    for stop in stops:
        stop_lat = float(stop.getLat())
        stop_lon = float(stop.getLon())

        stop_distance = calculateDistance(park_lat, park_lon, stop_lat, stop_lon)
        if stop_distance < distance:
            user_stop = stop
            distance = stop_distance

    if user_stop != False:
        print user_stop.getName(), user_stop.getLat(), user_stop.getLon()
