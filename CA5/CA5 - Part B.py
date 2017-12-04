#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
#Created on Sun Nov 26 13:51:23 2017

@author: muditkapoor 10352635
"""




def sum(values):
    return reduce(lambda x, y: x+y, values)


def add(first, second):
    return map(lambda x, y: x+y, first, second)	
	

def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
	
def is_even(values):
	return filter(lambda x: x%2==0, values)
	

def is_odd(values):
	return filter(lambda x: x%2, values)
	

def greater_than(values):
	mean = sum(values)/len(values)
	return filter(lambda x: x>mean, values)

	
def divide(first, second):
	return map(lambda x, y: x/float(y) if y!=0 else 'nan', first, second) 


def multiply(first, second):
	return map(lambda x, y: x*float(y) if y!=0 else 'nan', first, second) 	
	

def square(values):	
	return map(lambda x: x*x, values)

    
def expon(first, second):
    return map(lambda x, y: x**y, first, second)
        
        

def pythag(n):
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield(x,y,z)
					

def fibonacci(n):
	a = 0
	b = 1
	counter = 0
	while True:
		if (counter >= n): return
		yield a
		c = a
		a = b
		b = c + b
		counter += 1
	

print sum([47, 19, 20])
print add([4, 5, 11, 14, 15], [1, 9, 16, 21, 24])
print max([2, 6, 11, 12, 14, 19, 24, 42, 72])
print min([2, 6, 11, 12, 14, 19, 24, 42, 72])
print is_even([2, 6, 11, 12, 14, 19, 24, 42, 72])
print is_odd([2, 6, 11, 12, 14, 19, 24, 42, 72])
print greater_than([2, 6, 11, 12])
print divide([9, 66, 24],[3, 6, 8])
print multiply([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print square([2, 6, 11])
print expon([3, 6, 11], [2, 3, 4])

for trip in pythag(20):
	print trip,

for x in fibonacci(20):
	print x,