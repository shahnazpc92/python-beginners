# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:29:31 2019

@author: john
"""

tu1 =(12, -1.33, 'we', ['po', 31], 'ty', 4, -4.11 )
li1=[11, 7.1, 'io', -9, ('df', 6), 'yu', -6, -7.1 ]
print(li1)

print("First element from left side that is index no.", li1[0])
print("last element from right side is negative no.", li1[-1])

subli=li1[1:-1]          #from 1 to -1 formula(m:n-1)
print subli
subli=li1[-5:-1]        #from -5 to -1 then -1 decreases to 1
print subli
subli=li1[5:1]         # m < n
print subli
subli=li1[:2]         #no 'm' in m:n
print subli
subli=li1[2:]        #no 'n' in m:n
print subli
subli=li1           #no '[]'
print subli
   
li2 =li1         #Shallow Copy, Creates new Reference
li3 =li1[:]     #Deep Copy, Creates new Object or List    

print("li1 is", id(li1))
print("li2 is", id(li2))
print("li3 is", id(li3))

alpha= 'abcdefghijklmnopqrstuvwxyz'
print(alpha[3:23:2]) #Formula start:stop:step m:n-1:b