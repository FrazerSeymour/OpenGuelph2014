class Park:
    def __init__ (self,  name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        
    def getName(self):  return self.name
    def getLat(self):   return self.lat
    def getLon(self):   return self.lon


class Route:
    def __init__ (self,  name):
        self.name = name
        self.route = []
        
    def appendToRoute(self, item):
        self.route.append(item)
        
    def getName(self): return self.name
    def getRoute(self): return self.route

    def sortRoute(self):
        self.route.sort(key=lambda stop: stop[1])



class Stop:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.names = []
        self.routes = []
        
        
    def getLat(self):       return self.lat
    def getLon(self):       return self.lon
    def getNames(self):      return self.names
    def getRoutes(self):    return self.routes
    
    def addName(self, name):
        if not self.names.count(name):
            self.names.append(name)

    def addRoute(self, item):
        if not self.routes.count(item):
            self.routes.append(item)

