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
        
    def getName(self): return self.name
    def getRoute(self): return self.route
        
    def appendToRoute(self, item):
        self.route.append(item)



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
