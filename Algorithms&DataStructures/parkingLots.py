""" An object oriented design for a parking lot"""

from math import floor
from sqlite3 import Row
from typing_extensions import Self

def VehicleSize(Motorcycle, Compact, Large):
    pass

class Vehicle:
    parkingSpots = [] #array of parking spots

    def __init__(self, licensePlate, spotsNeeded, size):
        self.licensePlate = licensePlate
        self.spotsNeeded = spotsNeeded
        self.size = VehicleSize(size)

    def getSpotsNeeded(self):
        return self.spotsNeeded

    def getSize(self):
        VehicleSize()
        return self.size

    def parkInSpot(self, s):
        self.s = ParkingSpot(s)
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
        self.vehicle = Vehicle(vehicle)

    def parkStartingAtSpot(self, num, v):
        self.num = num
        self.v = Vehicle(v)

    def findAvailableSpots(self, vehicle):
        self.vehicle = Vehicle(vehicle)

    def spotFreed(self):
        self.availableSpots += 1

    
class ParkingSpot:
    def __init__(self, row, spotNumber, vehicle, spotSize, level):
        self.row = row 
        self.spotNumber = spotNumber
        self.vehicle = Vehicle(vehicle)
        self.spotSize = VehicleSize(spotSize)
        self.level = Level(level)

    def ParkingSpot(self, lvl, r, n, s):
        self.lvl = Level(lvl)
        self.r = r
        self.n = n
        self.s = VehicleSize(s)

    def isAvailable(self):
        self.vehicle == None
        return self.vehicle

    def canFitVehicle(self, vehicle):
        self.vehicle = Vehicle(vehicle)

    def park(self, v):
        self.v = Vehicle(v)

    def getRow(self):
        return self.row

    def getSpotNumber(self):
        return self.spotNumber

    def removeVehicle(self):
        pass

        


        
