""" An object oriented design for a parking lot"""

class Vehicle:
    parkingSpots = [] #array of parking spots

    def __init__(self, licensePlate, spotsNeeded, size):
        self.licensePlate = licensePlate
        self.spotsNeeded = spotsNeeded
        self.size = size

    def getSpotsNeeded(self):
        return self.spotsNeeded

    def getSize(self):
        return self.size

    def parkInSpot(self, s):
        self.s = s
        self.parkingSpots.add(s)

    def clearSpots(self):
        pass 

    def canFitInSpot(self, spot):
        self.spot = spot
        self.parkingSpots = self.parkingSpots(spot)
