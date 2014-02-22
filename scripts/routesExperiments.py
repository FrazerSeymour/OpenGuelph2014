from pickle import load

class Route:
    def __init__ (self,  name):
        self.name = name
        self.route = []
        
    def appendToRoute(self, item):
        self.route.append(item)
        
    def getName(self): return self.name
    def getRoute(self): return self.route

if __name__ == "__main__":
    f = open("./resources/routes.pickle", 'r')
    routes = load(f)
    f.close()

    for route in routes:
        print route.getName()
