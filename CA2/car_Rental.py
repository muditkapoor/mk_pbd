import random
from collections import deque
from Car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

class CarRental(object):

    
    def __init__(self):
        self.available_cars = dict()
        self.rented_cars = dict()
        self._colours = ('Silver', 'Black', 'Blue', 'Grey')
        self._make = ('Toyota', 'BMW', 'Nissan')
        self.type_IDs = ('P', 'D', 'E', 'H')
        
   
    def create_cars(self, num, type):
        car_list = deque()
        for i in range(num):
            car = type()
            car.setColour(random.choice(self._colours))
            car.setMake(random.choice(self._make))
            car.setMileage(random.randrange(0, 10000))
            car_list.append(car)
        return car_list
    
   
    def create_stock(self):
        self.available_cars['P'] = self.create_cars(24, PetrolCar)
        self.available_cars['D'] = self.create_cars(8, DieselCar)
        self.available_cars['E'] = self.create_cars(4, ElectricCar)
        self.available_cars['H'] = self.create_cars(4, HybridCar)
    
  
    def count_stock(self, type_ID):
        return len(self.available_cars[type_ID])
    
   
    def is_in_stock(self, type_ID, num):
        if type_ID in self.type_IDs and isinstance(num, int):
            return num <= self.count_stock(type_ID)
        else:
            raise ValueError
    
   
    def get_car(self, type_ID):
        if type_ID in self.type_IDs:
            return self.available_cars[type_ID].popleft()
        else:
            raise ValueError    
        
   
    def check_car_type(self, car):
        if isinstance(car, PetrolCar):
            return 'P'
        elif isinstance(car, DieselCar):
            return 'D'
        elif isinstance(car, ElectricCar):
            return 'E'
        elif isinstance(car, HybridCar):        
            return 'H'
        else:
            raise ValueError
    
  
    def get_booking_list(self, num_cars, type_ID):
        if  isinstance(num_cars, int) and type_ID in self.type_IDs:
            booking_list = list()
            for i in range(num_cars):
                rented_car = self.get_car(type_ID) 
                booking_list.append(rented_car)
            return booking_list
        else:
            raise ValueError
    
   
    def process_rental(self, num_cars, type_ID, cust_name):        
        booking_ref = random.randrange(1000, 2000)
        booking_list = self.get_booking_list(num_cars, type_ID)
        self.rented_cars[booking_ref] = {'car': booking_list, 'customer name': cust_name } 
        return booking_ref 

   
    def process_return(self, ref):
        booking = self.rented_cars.pop(ref)
        for car in booking['car']:
            type_ID = self.check_car_type(car)
            self.available_cars[type_ID].append(car) 