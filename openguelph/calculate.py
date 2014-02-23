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



def getNextTime(stop, route):
    time = datetime.now()

    current_yr = time.year
    current_month = time.month
    current_day = time.day

    fmt = "%H:%M:%S"

    distance = 84600
    best_time = False

    for route_stop in route.getRoute():
        stop_name = route_stop[0]
        
        stop_time = route_stop[2]
        split_time = stop_time.split(':')
        stop_hr = int(split_time[0])
        stop_min = int(split_time[1])
        stop_sec = int(split_time[2])
        stop_time = datetime(year = current_yr, month = current_month, day = current_day, hour = stop_hr, minute = stop_min)

        diff = stop_time - time

        if stop_name == stop and diff.total_seconds() > 0 and diff.total_seconds() < distance:
            distance = diff.total_seconds()
            best_time = route_stop[2]

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



def getRoute(prefix, routes):
    # Find possible routes.
    possibilities = []
    for route in routes:
        if prefix in route.getName():
            possibilities.append(route)

   # If only a weekday bus.
    if len(possibilities) == 1:
        return possibilities[0]

    # Else:
    else:
        date = datetime.today()
        day = date.weekday()

        if day == 0:
            for possibility in possibilities:
                if "sunday" in possibility.getName():
                    return possibility

        elif day == 6:
            for possibility in possibilities:
                if "saturday" in possibility.getName():
                    return possibility

        else:
            for possibility in possibilities:
                if "weekday" in possibility.getName():
                    return possibility
