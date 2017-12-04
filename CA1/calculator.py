#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:13:20 2017

@author: muditkapoor 10352635
"""

'''Below functions used for Scientific Calculator Program'''


def add (first, second):        
    return first + second

    
def subtract (first, second):   
    return first - second


def multiply (first, second):   
    return first * second

 
def divide (first, second):     
    return first / second


def exponentiate (first, second):   
    return first ** second


def squareRoot(first):          
    return first ** (0.5)


def cube(first):                
    return first ** 3
    

def cubeRoot(first):             
    return first ** (1.0 / 3)


def factorial(n):               
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        return res
    
 
def sine(n):
    x = n * 0.017455329
    sin = x - (x**3)/factorial(3) + (x**5)/factorial(5) - (x**7)/factorial(7) + (x**9)/factorial(9) - (x**11)/factorial(11) + (x**13)/factorial(13) - (x**15)/factorial(15) + (x**17)/factorial(17) - (x**19)/factorial(19) 
    return sin

   
def cosine(n):
    x = n * 0.017455329
    cos = 1 - (x**2)/factorial(2) + (x**4)/factorial(4) - (x**6)/factorial(6) + (x**8)/factorial(8) - (x**10)/factorial(10) + (x**12)/factorial(12) - (x**14)/factorial(14) + (x**16)/factorial(16) - (x**18)/factorial(18) 
    return cos