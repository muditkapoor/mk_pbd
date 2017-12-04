#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:14:42 2017

@author: muditkapoor 10352635
"""

import unittest

#Importing all defined scientific functions from calculator.py

from calculator import *


class Test_Calculator(unittest.TestCase):

  
    def test_add(self):
        self.assertEqual(add(3,4),7)                    #Testing 3 + 4 = 7
        self.assertEqual(add(-3,4),1)                   #Testing -3 + 4 = 1
        self.assertEqual(add(30,-40),-10)               #Testing 30 + (-40) = -10
        
    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)               #Testing 5 - 3 = 2
        self.assertEqual(subtract(5,-3),8)              #Testing 5 - (-3) = 8
        self.assertEqual(subtract(-5,3),-8)             #Testing -5 - 3 = -8
        
    def test_multiply(self):
        self.assertEqual(multiply(5,3),15)              #Testing 5 * 3 = 15
        self.assertEqual(multiply(5,-3),-15)            #Testing 5 * -3 = -15
        self.assertEqual(multiply(-5,-3),15)            #Testing -5 * -3 = 15
        
    def test_divide(self):
        self.assertEqual(divide(6,3),2)                 #Testing 6 / 3 = 2
        self.assertEqual(divide(6,-3),-2)               #Testing 6 / -3 = -2
        self.assertEqual(divide(-6,-3),2)               #Testing 6 / -3 = 2
        
    def test_exponentiate(self):
        self.assertEqual(exponentiate(2,5),32)          #Testing 2 ** 5 = 32
        self.assertEqual(exponentiate(3,4),81)          #Testing 3 ** 4 = 81
        self.assertEqual(exponentiate(10,3),1000)       #Testing 10 ** 3 = 1000
        
    def test_squareRoot(self):
        self.assertEqual(squareRoot(49),7)              #Testing Square Root of 49 = 7
        self.assertEqual(squareRoot(100),10)            #Testing Square Root of 100 = 10
        self.assertEqual(squareRoot(81),9)              #Testing Square Root of 81 = 9
        
    def test_cube(self):
        self.assertEqual(cube(5),125)                   #Testing 5 ** 3 = 125
        self.assertEqual(cube(4),64)                    #Testing 4 ** 3 = 64
        self.assertEqual(cube(2),8)                     #Testing 2 ** 3 = 8
       
    def test_cubeRoot(self):
        self.assertEqual(round(cubeRoot(125),5),5)      #Testing Cube Root of 125 = 5
        self.assertEqual(round(cubeRoot(27),5),3)       #Testing Cube Root of 27 = 3
        self.assertEqual(round(cubeRoot(1000),5),10)    #Testing Cube Root of 1000 = 10
        
    def test_factorial(self):
        self.assertEqual(factorial(5),120)              #Testing 5! = 120
        self.assertEqual(factorial(3),6)                #Testing 3! = 6    
        self.assertEqual(factorial(4),24)               #Testing 4! = 24
    
    def test_sine(self):
        self.assertEqual(round(sine(90),5), 1)          #Testing Sin of 90 degrees = 1
        self.assertEqual(round(sine(45),5), 0.70717)    #Testing Sin of 45 degrees = 0.70717
        self.assertEqual(round(sine(30),3), 0.5)        #Testing Sin of 30 degrees = 0.5
        
    def test_cosine(self):
        self.assertEqual(round(cosine(0),2), 1)         #Testing Cos of 0 degrees = 1
        self.assertEqual(round(cosine(45),3), 0.707)    #Testing Cos of 45 degrees = 0.707
        self.assertEqual(round(cosine(60),1), 0.5)      #Testing Cos of 60 degrees = 0.5
        
        
if __name__ == '__main__':
    unittest.main()