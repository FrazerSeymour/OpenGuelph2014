from pickle import dump
import xml.etree.ElementTree as ET

class Park:
    def __init__ (self,  name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        
    def getName(self):  return self.name
    def getLat(self):   return self.lat
    def getLon(self):   return self.lon



if __name__ == "__main__":
    parks = []
   
    tree = ET.parse("./resources/parks.xml")
    root = tree.getroot()

    for child in root:
        name = child.find("ParkName").text
        lat = child.find("Latitude").text
        lon = child.find("Longitude").text

        parks.append(Park(name, lat, lon))


    f = open("./resources/parks.pickle", 'w')
    dump(parks, f)
    f.close()
