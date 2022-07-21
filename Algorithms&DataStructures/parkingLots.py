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

        class Bus(Vehicle):
    def Bus(self):
        self.spotsNeeded = 5
        self.size = self.VehicleSize.Large 

    def canFitInSpot(self, spot):
        return super().canFitInSpot(spot)
    
class Bus(Vehicle):
    def Bus(self):
        self.spotsNeeded = 5
        self.size = self.VehicleSize.Large 

    def canFitInSpot(self, spot):
        return super().canFitInSpot(spot)

class Car(Vehicle):
    def Car(self):
        self.spotsNeeded = 1
        self.size = self.VehicleSize.Compact

    def canFitInSpot(self, spot):
        return super().canFitInSpot(spot)

class Motorcycle(Vehicle):
    def Motorcycle(self):
        self.spotsNeeded = 1
        self.size = self.VehicleSize.Motorcycle

    def canFitInSpot(self, spot):
        return super().canFitInSpot(spot)
    
class ParkingLot:
    def __init__(self):
        self.levels = []
        self.num_levels = 5

    def ParkingLot(self):
        pass

    def parkVehicle(self, vehicle):
        return Vehicle(vehicle)
    
class Level:
    def __init__(self):
        self.floor = floor
        self.spot = []
        self.availableSpots = 0
        self.SPOTS_PER_ROW = 10

    def level(self, flr, numberSpots):
        self.flr = flr
        self.numberSpots = numberSpots

    def availableSpots(self):
        return self.availableSpots

    def parkVehicle(self, vehicle):
        pass
