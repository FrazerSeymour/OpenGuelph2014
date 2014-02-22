from pickle import load

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
    f = open("./resources/stops.pickle", 'r')
    stops = load(f)
    f.close()

    routes = ["2A", "Route2B", "Route3B", "Route4", "Route10", "Route11", "Route14", "Route20", "Route21", "Route1A", "Route1B", "Route12", "Route6", "Route7", "Route13", "Route3A", "Route5", "Route15", "Route8", "Route9", "Route56", "Route57", "Route58", "Route50", "Route16", "Route Gordon Corridor"]

    for stop in stops:
        for route in stop.getRoutes():
            if route not in routes:
                print route

    #stopNames = []
    #for stop in stops:
    #    stopNames.append(stop.getName())

    #words = []
    #for name in stopNames:
    #    wordsTemp = name.split(" ")
    #    for word in wordsTemp:
    #        if (not "." in word) and (not words.count(word)):
    #            words.append(word)

    #for word in words:
    #    print word
