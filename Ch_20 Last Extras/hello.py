# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:50:31 2019

@author: john
"""

x=5     # An Integer
y="Hello"
z=4.15
if x < 8:
    print("Yes")
    print("Hello")
    y=y+'World'
    
print("Done")
print(y)

print "Type of x is", type(x)
print "Type of y is", type(y)
if type(x) is int:
    print("Integer")
    
print ("It's there (In this if we want to put ' need to be written in double quote)")
print ('"Hello", He Said(In this if we want to put " need to be written in single quote)')
print (''' "It's there", He Said (For both)''')