
class Car(object):
   

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = '' 
    

    def getColour(self):
        return self.__colour
    

    def getMileage(self):
        return self.__mileage
    

    def getMake(self):
        return self.__make
    

    def setColour(self, colour):
        self.__colour = colour

       
    def setMileage(self, mileage):
        if isinstance(mileage, (int, float)):
            self.__mileage = mileage
        else:
            raise ValueError
            
      
    def setMake(self, make):
        self.__make = make


class ElectricCar(Car):
  

    def __init__(self):	
        Car.__init__(self)
        self.__numberFuelCells = 1
    

    def getNumberFuelCells(self):
        return self.__numberFuelCells 
    
	
    def setNumberFuelCells(self, value):
        if isinstance(value, (int, float)):
            self.__numberFuelCells = value
        else:
            raise ValueError


class PetrolCar(Car):
   

    def __init__(self):	
        Car.__init__(self)
        self.__numberCylinders = 8
    

    def getNumberCylinders(self):
        return self.__numberCylinders
    
    
    def setNumberCylinders(self, value):
        if isinstance(value, (int, float)):
            self.__numberCylinders = value
        else:
            raise ValueError

class DieselCar(Car):


    def __init__(self):
        Car.__init__(self)
        self.__numberGlowPlugs = 1
     

    def getNumberGlowPlugs(self):
        return self.__numberGlowPlugs

      
    def setNumberGlowPlugs(self, value):
        if isinstance(value, (int, float)):
            self.__numberGlowPlugs = value
        else:
            raise ValueError
        
        
class HybridCar(Car):


    def __init__(self):
        Car.__init__(self)
        self.__typeHybridBattery = 'Lithium-Ion'
    

    def getTypeHybridBattery(self):
        return self.__typeHybridBattery
        
      
    def setTypeHybridBattery(self, value): 
        self.__typeHybridBattery = value