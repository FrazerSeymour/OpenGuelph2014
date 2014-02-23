class Park:
    def __init__ (self,  name, summary, address, description, lat, lon):
        self.name = name
        self.summary = summary
        self.address = address
        self.description = description
        self.lat = lat
        self.lon = lon

    def getAddress(self):   return self.address
    def getDescription(self):   return self.description
    def getLat(self):       return self.lat
    def getLon(self):       return self.lon
    def getName(self):      return self.name
    def getSummary(self):   return self.summary



class Place:
    def __init__ (self,  name, summary, address, description, lat, lon, dt_route, dt_path, uc_route, uc_path):
        self.name = name
        self.summary = summary
        self.address = address
        self.description = description
        self.lat = lat
        self.lon = lon
        self.dt_route = dt_route
        self.dt_path = dt_path
        self.uc_route = uc_route
        self.uc_path = uc_path

    def getAddress(self):   return self.address
    def getDescription(self):   return self.description
    def getDtPath(self):    return self.dt_path
    def getDtRoute(self):   return self.dt_route
    def getLat(self):       return self.lat
    def getLon(self):       return self.lon
    def getName(self):      return self.name
    def getSummary(self):   return self.summary
    def getUcPath(self):    return self.uc_path
    def getUcRoute(self):   return self.uc_route



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

