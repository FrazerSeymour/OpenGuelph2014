from csv import reader
from pickle import dump

class Stop:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.routes = []
        
        
    def getName(self):      return self.name
    def getLat(self):       return self.lat
    def getLon(self):       return self.lon
    def getRoutes(self):    return self.routes
    
    def addRoute(self, item):
        if not self.routes.count(item):
            self.routes.append(item)




if __name__ == "__main__":
    stops = []
    
    with open("./resources/busGTFS/stops.txt", 'r') as csvfile:
        csvreader = reader(csvfile)

        positions = []
        for row in csvreader:
            try:
                name = row[2]
                name = name.upper()
                name = name.replace(".", "")

                lat = row[4]
                lon = row[5]

                if not positions.count([lat, lon]):
                    positions.append([lat, lon])
                    stops.append(Stop(name, lat, lon))

                route = row[0].split("-")[0]
                if route == "Route":
                    route = "Route Gordon Corridor"
                for stop in stops:
                    if lat == stop.getLat() and lon == stop.getLon():
                        stop.addRoute(route)
                

            except:
                pass
        
        csvfile.close()
        
    f = open("./resources/stops.pickle", 'w')
    dump(stops, f)
    f.close()
