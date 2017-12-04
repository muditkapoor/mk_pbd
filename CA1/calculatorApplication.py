#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:12:55 2017

@author: muditkapoor 10352635
"""

from calculator import *

def show_menu():
   print "##########################"
   print "Enter 1 for Addition"
   print "Enter 2 for Subtraction"
   print "Enter 3 for Multiplication"
   print "Enter 4 for Division"
   print "Enter 5 for Exponentiate"
   print "Enter 6 for Square Root"
   print "Enter 7 for Cube"
   print "Enter 8 for Cube Root"
   print "Enter 9 for Factorial"
   print "Enter 10 for Sine"
   print "Enter 11 for Cosine"
   print "Enter 12 for Tangent" 
   print "Q to quit"
   print "###########################"


while True:
    show_menu()
    str_input = raw_input("Please input your menu choice >")
    if str_input.upper() == 'Q':
        break
        
      
    try:
        choice = int(str_input)
    except:
        print 'Invalid input'
        raw_input("Press 'Enter' to go back to the main menu >")
        continue
        
        
    if choice < 1 or choice >= 13:
        print 'Invalid input'
        raw_input("Press 'Enter' to go back to the main menu >")
        continue

         
    elif choice >= 1 and choice <= 5:
        str_input1 = raw_input('Please enter first number for calculation >')
        str_input2 = raw_input('Please enter second number for calculation >')

        
        try:
            num1 = float(str_input1)
            num2 = float(str_input2)
       
        except:
            print 'Invalid input'
            raw_input("Press 'Enter' to go the main menu >")
            continue

           
    elif choice >= 6 and choice <= 12:
        number1 = raw_input('Please Enter number for calculation >')
        

        try:
            number1 = float(number1)
        except:
            print 'Invalid input'
            raw_input("Press 'Enter' to go to the main menu >")
            continue 

            
    if choice == 1:
        print add (num1, num2)
       
    elif choice == 2:
        print subtract (num1, num2)
      
    elif choice == 3:
        print multiply (num1, num2)
       
    elif choice == 4:
        print divide (num1, num2)
       
    elif choice == 5:
        print exponentiate (num1, num2)
       
    elif choice == 6:
        print squareRoot (number1)
       
    elif choice == 7:
        print cube (number1)
       
    elif choice == 8:
        print cubeRoot (number1)
             
    elif choice == 9:
        print factorial (number1)
       
    elif choice == 10:
        print sine (number1)
       
    elif choice == 11:
        print cosine (number1)
        
    elif choice == 12:
        print sine (number1)/cosine (number1)
       
       
    if 'Q' == raw_input("Type Q to quit or Enter to continue >"):
        break

        
print "Thank you for using Python calculator"