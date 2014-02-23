from pickle import dump
import xml.etree.ElementTree as ET

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



if __name__ == "__main__":
    parks = []
   
    tree = ET.parse("./resources/parks.xml")
    root = tree.getroot()

    for child in root:
        name = child.find("ParkName").text.title()
        if name[-1] == " ":
            name = name[:-1]

        summary = child.find("ParkType").text
        address = child.find("Address").text
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet molestie libero. Vivamus ullamcorper est vel blandit pellentesque. Sed eu purus ac neque fermentum eleifend et eget velit. Ut neque ipsum, vehicula et tortor ut, imperdiet tempus dui. Cras scelerisque elementum commodo."
        lat = child.find("Latitude").text
        lon = child.find("Longitude").text

        parks.append(Park(name, summary, address, description, lat, lon))


    f = open("./resources/parks.pickle", 'w')
    dump(parks, f)
    f.close()
