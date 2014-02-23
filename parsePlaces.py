from openguelph.calculations import *
from openguelph.classes import *
from pickle import dump



def fastestTry(tries):
    time = datetime.now()
    current_yr = time.year
    current_month = time.month
    current_day = time.day

    lowest = 10000
    lowestTry = None
    for tri in tries:
        if tri[1] != []:
            split_time = tri[1][0][1].split(':')
            stop_hr = int(split_time[0])
            stop_min = int(split_time[1])
            stop_sec = int(split_time[2])
            depart_time = datetime(year = current_yr, month = current_month, day = current_day, hour = stop_hr, minute = stop_min)

            split_time = tri[1][-1][1].split(':')
            stop_hr = int(split_time[0])
            stop_min = int(split_time[1])
            stop_sec = int(split_time[2])
            arrive_time = datetime(year = current_yr, month = current_month, day = current_day, hour = stop_hr, minute = stop_min)
            diff = arrive_time - depart_time
            diff = diff.total_seconds()

            if diff < lowest:
                lowestTry = tri
                lowest = diff

    return lowestTry




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



def tryRoute(destination, stop, route, routes):
    routeName = getRoute(route, routes)
    time = getNextTime(destination, routeName)
    path = getPath(routeName, destination, time, stop)
    return [routeName, path]


if __name__ == "__main__":
    parks, routes, stops = openData()

    places = []

    for park in parks:
        # Get some values.
        name = park.getName()
        summary = park.getSummary()
        address = park.getAddress()
        description = park.getDescription()

        # Determine the closest bus stop.
        lat = float(park.getLat())
        lon = float(park.getLon())
        user_stops = getNearestStops(lat, lon, stops)

        dt_tries = []
        uc_tries = []

        for stop in user_stops:
            if stop != False:
                for route in stop.getRoutes():
                    dt_tries.append(tryRoute("Guelph Central Station", stop, route, routes))
                    uc_tries.append(tryRoute("University Centre", stop, route, routes))

        try:
            dt_route, dt_path = fastestTry(dt_tries)
        except:
            dt_route, dt_path = False, False
        try:
            uc_route, uc_path = fastestTry(uc_tries)
        except:
            uc_route, uc_path = False, False

        places.append(Place(name, summary, address, description, lat, lon, dt_route, dt_path, uc_route, uc_path))

    # Pickle
    f = open("./places.pickle", 'w')
    dump(places, f)
    f.close()

