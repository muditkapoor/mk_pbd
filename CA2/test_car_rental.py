# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 15:37:12 2017

@author: mk2
"""

import unittest
from collections import deque
from car_Rental import CarRental
from Car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
     

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.setMileage(15000)
        self.assertEqual(15000, self.car.getMileage())
        self.assertRaises(ValueError, self.car.setMileage, '2')
        self.assertRaises(TypeError, self.car.setMileage, 10000, 1500)
    

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Masarati')
        self.assertEqual('Masarati', self.car.getMake())
        self.assertRaises(TypeError, self.car.getMake, 'Masarati')
        self.assertRaises(TypeError, self.car.getMake, 'Masarati', 'One')
    

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.setColour('Silver')
        self.assertEqual('Silver', self.car.getColour())
        self.assertRaises(TypeError, self.car.getColour, 'blue')
        self.assertRaises(TypeError, self.car.setColour, 'blue', 'green')
        

class TestElectricCar(unittest.TestCase):

    def setUp(self):
        self.electric_car = ElectricCar()	
    

    def test_electric_car_fuel_cells(self):
        self.assertEqual(1, self.electric_car.getNumberFuelCells())
        self.electric_car.setNumberFuelCells(8)
        self.assertEqual(8, self.electric_car.getNumberFuelCells())
        self.assertRaises(ValueError, self.electric_car.setNumberFuelCells, '6')
        self.assertRaises(TypeError, self.electric_car.setNumberFuelCells, 2, 4)
    

    def test_electric_car_mileage(self):
        self.assertEqual(0, self.electric_car.getMileage())
        self.electric_car.setMileage(460000)
        self.assertEqual(460000, self.electric_car.getMileage())
        self.assertRaises(ValueError, self.electric_car.setMileage, '60000')

     
class TestPetrolCar(unittest.TestCase):
            
    def setUp(self):
        self.petrol_car = PetrolCar()


    def test_petrol_car_cylinders(self):
        self.assertEqual(8, self.petrol_car.getNumberCylinders())
        self.petrol_car.setNumberCylinders(16)
        self.assertEqual(16, self.petrol_car.getNumberCylinders())
        self.assertRaises(ValueError, self.petrol_car.setNumberCylinders, '12')
        self.assertRaises(TypeError, self.petrol_car.setNumberCylinders, 12, 6)
    

    def test_petrol_car_make(self):
        self.assertEqual('', self.petrol_car.getMake())
        self.petrol_car.setMake('Ford')
        self.assertEqual('Ford', self.petrol_car.getMake())

   
class TestDieselCar(unittest.TestCase):  
    
    def setUp(self):
        self.diesel_car = DieselCar()
    

    def test_diesel_car_glow_plugs(self):
        self.assertEqual(1, self.diesel_car.getNumberGlowPlugs())
        self.diesel_car.setNumberGlowPlugs(6)
        self.assertEqual(6, self.diesel_car.getNumberGlowPlugs())
        self.assertRaises(ValueError, self.diesel_car.setNumberGlowPlugs, 'six')
        self.assertRaises(TypeError, self.diesel_car.setNumberGlowPlugs, 'six', 2)

     
class TestHybridCar(unittest.TestCase):
    

    def setUp(self):
        self.hybrid_car = HybridCar()
    

    def test_hybrid_car_hybrid_battery(self):
        self.assertEqual('Lithium-Ion', self.hybrid_car.getTypeHybridBattery())
        self.hybrid_car.setTypeHybridBattery('Nickel-Metal Hydride')
        self.assertEqual('Nickel-Metal Hydride', self.hybrid_car.getTypeHybridBattery())
        self.assertRaises(TypeError, self.hybrid_car.getTypeHybridBattery, 1)
        self.assertRaises(TypeError, self.hybrid_car.setTypeHybridBattery, 'battery', 'another type')

    
class TestCarRental(unittest.TestCase):


    def setUp(self):
        self.rental = CarRental()
        self.rental.create_stock()
        self.rental.test_ref = self.rental.process_rental(3, 'P', 'John Black')
    

    def test_create_cars(self):
        car_deque = self.rental.create_cars(20, PetrolCar)
        self.assertEqual(20, len(car_deque))
        self.assertTrue(all(isinstance(car, PetrolCar) for car in car_deque))
        self.assertTrue(all(car.getMake != '' for car in car_deque))
        self.assertRaises(TypeError, self.rental.create_cars, 20, PetrolCar, 2)
        self.assertRaises(TypeError, self.rental.create_cars, 20, 2)
    

    def test_create_stock(self):
        self.assertEqual(4, len(self.rental.available_cars))
        self.assertTrue(all(isinstance(value, deque) for value in self.rental.available_cars.values()))
        self.assertEqual(21, len(self.rental.available_cars['P']))
        self.assertEqual(8, len(self.rental.available_cars['D']))
        self.assertEqual(4, len(self.rental.available_cars['E']))
        self.assertEqual(4, len(self.rental.available_cars['H']))


    def test_count_stock(self):
        self.assertEqual(4, self.rental.count_stock('H'))
        self.assertEqual(8, self.rental.count_stock('D'))
        self.assertEqual(4, self.rental.count_stock('E'))
        self.assertEqual(21, self.rental.count_stock('P'))


    def test_is_in_stock(self): 
        self.assertTrue(self.rental.is_in_stock('P', 5))
        self.assertTrue(self.rental.is_in_stock('D', 8))
        self.assertFalse(self.rental.is_in_stock('H', 10))
        self.assertRaises(ValueError, self.rental.is_in_stock, HybridCar, 10)
        

    def test_get_car(self): 
        self.assertEqual(PetrolCar, type(self.rental.get_car('P')))
        self.assertNotEqual(PetrolCar, type(self.rental.get_car('H')))
        self.assertRaises(ValueError, self.rental.get_car, 'Hybrid')
        

    def test_check_car_type(self): 
       self.assertEqual('E', self.rental.check_car_type(ElectricCar()))
       self.assertRaises(ValueError, self.rental.check_car_type, 'Electric')


    def get_booking_list(self): 
        test_list = self.rental.get_booking_list(5, 'D')
        self.assertEqual(5, len(test_list))
        self.assertTrue(all(isinstance(car, DieselCar) for car in test_list))
        self.assertRaises(ValueError, self.rental.get_booking_list('5', 'D'))
        

    def test_process_rental(self):   
        self.assertIsInstance(self.rental.test_ref, int)
        self.assertEqual(3, len(self.rental.rented_cars[self.rental.test_ref]['car']))
        self.assertTrue(all(isinstance(car, PetrolCar) for car in self.rental.rented_cars[self.rental.test_ref]['car']))
        self.assertEqual('John Black', self.rental.rented_cars[self.rental.test_ref]['customer name'])
        self.assertEqual(21, len(self.rental.available_cars['P']))
        self.assertRaises(TypeError, self.rental.process_rental, 4, 'H')
    

    def test_process_return(self):
        self.rental.process_return(self.rental.test_ref)
        self.assertEquals(0, len(self.rental.rented_cars))
        self.assertEquals(24, len(self.rental.available_cars['P']))

if __name__ == '__main__':
    unittest.main()