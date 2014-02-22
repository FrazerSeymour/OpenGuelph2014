from openguelph.classes import *
from pickle import load

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
