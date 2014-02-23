from datetime import datetime
from math import sqrt
from openguelph.classes import *
from pickle import load

def calculateDistance(x1, y1, x2, y2):
    x = (x1 - x2)
    x = x * x
    y = (y1 - y2)
    y = y * y
    return sqrt(x + y)



def getNearestStop(lat, lon, stops):
    distance = 100
    user_stop = False

    for stop in stops:
        stop_lat = float(stop.getLat())
        stop_lon = float(stop.getLon())

        stop_distance = calculateDistance(park_lat, park_lon, stop_lat, stop_lon)
        if stop_distance < distance:
            user_stop = stop
            distance = stop_distance

    return user_stop



def openData():
    f = open("./resources/parks.pickle", 'r')
    parks = load(f)
    f.close()

    f = open("./resources/routes.pickle", 'r')
    routes = load(f)
    f.close()

    f = open("./resources/stops.pickle", 'r')
    stops = load(f)
    f.close()

    return parks, routes, stops



def getNextTime(stop, route):
    time = datetime.now().time()
    current_hr = time.hour
    current_min = time.minute
    current_sec = time.second

    distance = [24, 60, 60]
    best_time = False

    for route_stop in route.getRoute():
        stop_name = route_stop[0]
        stop_time = route_stop[2]
        
        stop_hr = int(stop_time[0:2])
        stop_min = int(stop_time[3:5])
        stop_sec = int(stop_time[6:8])
        
        distance_hr = stop_hr - current_hr
        distance_min = stop_min - current_min
        distance_sec = stop_sec - current_sec
        
        if route_stop[0] == stop and distance_hr >= 0 and distance_min >= 0:
                if distance_hr <= distance[0] and distance_min <= distance[1]:
                    distance = [distance_hr, distance_min, distance_sec]
                    best_time = stop_time
                    
                    
    return best_time



if __name__ == "__main__":
    parks, routes, stops = openData()

    user_input = raw_input("Type in the name of a park: ")
    user_park = False
    for park in parks:
        if park.getName() == user_input.upper():
            user_park = park
            
    if user_park != False:
        print user_park.getName(), user_park.getLat(), user_park.getLon()

    park_lat = float(user_park.getLat())
    park_lon = float(user_park.getLon())
    
    user_stop = getNearestStop(park_lat, park_lon, stops)


    if user_stop:
        uc_time = getNextTime("University Centre", routes[0])
        if uc_time:
            print "Next bus from University Centre is at", uc_time

        dt_time = getNextTime("Guelph Central Station", routes[0])
        if dt_time:
            print "Next bus from Guelph Central Station is at", dt_time
