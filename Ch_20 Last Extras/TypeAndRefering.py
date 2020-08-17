# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:23:00 2019

@author: john
"""

x=30
y=12.71
z="Hello"

print('x is', type(x))
print('z is', z)
if x<25:
    x=x+1
    z=z+"world"
    
print('x is', x)
print('z is', z)
w=x     
x="hi"
print('x is',type(x))
w=x
y,x=x,y