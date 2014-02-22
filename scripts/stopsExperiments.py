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

    for stop in stops:
        if len(stop.getRoutes()) > 1:
            print stop.getName() ,
            for i in stop.getRoutes():
                print i ,
            print ""

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
