from datetime import datetime
from difflib import get_close_matches
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
        split_time = stop_time.split(':')

        stop_hr = int(split_time[0])
        stop_min = int(split_time[1])
        stop_sec = int(split_time[2])
        
        distance_hr = stop_hr - current_hr
        distance_min = stop_min - current_min
        distance_sec = stop_sec - current_sec

        if stop_name == stop and (distance_hr > 0 or (distance_hr == current_hr and distance_min >= 0)):
                if distance_hr <= distance[0] or (distance_hr == distance[0] and distance_min <= distance[1]):
                    distance = [distance_hr, distance_min, distance_sec]
                    best_time = stop_time
                    
                    
    return best_time



def getPath(route, depart_name, depart_time, destination):
    path = []

    stops = route.getRoute()
    add = False

    for stop in stops:
        stop_name = stop[0]
        stop_time = stop[2]

        if add == True:
            if destination.getNames().count(stop_name):
                add = False
            path.append([stop_name, stop_time])

        if stop_name == depart_name and stop_time == depart_time:
            add = True
            path.append([stop_name, stop_time])

    return path



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
        uc_time = getNextTime("University Centre", routes[9])
        if uc_time != False:
            print "Next bus from University Centre is at", uc_time

        uc_path = getPath(routes[9], "University Centre", uc_time, user_stop)
        if uc_path != []:
            for stop in uc_path:
                print stop[0], stop[1]

        dt_time = getNextTime("Guelph Central Station", routes[9])
        if dt_time != False:
            print "Next bus from Guelph Central Station is at", dt_time
        
        dt_path = getPath(routes[9], "Guelph Central Station", dt_time, user_stop)
        if dt_path != []:
            for stop in dt_path:
                print stop[0], stop[1]
