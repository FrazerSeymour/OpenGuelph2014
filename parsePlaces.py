from openguelph.calculations import *
from openguelph.classes import *
from pickle import dump



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
        user_stop = getNearestStop(lat, lon, stops)

        # Determine the bus route.
        route = getRoute(user_stop.getRoutes()[0], routes)

        # Determine the next departure times.
        uc_time = getNextTime("University Centre", route)
        dt_time = getNextTime("Guelph Central Station", route)

        # Determine the routes paths.
        if uc_time != False:
            uc_path = getPath(route, "University Centre", uc_time, user_stop)
        else:
            uc_path = []

        if dt_time != False:
            dt_path = getPath(route, "Guelph Central Station", dt_time, user_stop)
        else:
            dt_path = []

        places.append(Place(name, summary, address, description, lat, lon, route, dt_path, route, uc_path))

    # Pickle
    f = open("./places.pickle", 'w')
    dump(places, f)
    f.close()

