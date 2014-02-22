### This script goes through the 'stop_times' file, creating classes for each
### route and pickling them.

from csv import reader
from pickle import dump

### Information for a Guelph bus route.
#
# Contains the title of the route, an array containing the titles of the stops,
# and a list containing the full route in order.
class Route:
    def __init__ (self,  name):
        self.name = name
        self.route = []
        
    def appendToRoute(self, item):
        self.route.append(item)
        
    def getName(self): return self.name
    def getRoute(self): return self.route

if __name__ == "__main__":
    routes = []
    
    with open("./resources/busGTFS/stop_times.txt", 'r') as csvfile:
        csvreader = reader(csvfile)

        names = []
        for row in csvreader:
            try:
                nameBits = row[0].split('_')
                nameBits.pop()
                nameBits.pop()
                name = nameBits[0] + " " + nameBits[1]

                if not names.count(name):
                    names.append(name)
                    routes.append(Route(name))

                stopName = row[3].split('_')[1].title()
                for route in routes:
                    if name == route.getName():
                        route.appendToRoute([stopName, row[1], row[2]])


            except:
                pass
        
        csvfile.close()

    f = open("./resources/routes.pickle", 'w')
    dump(routes, f)
    f.close()
