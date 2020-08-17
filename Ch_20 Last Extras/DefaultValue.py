# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:40:48 2019

@author: john
"""

def defval(b, c=4,d="hi"):
    print d
    return b+c

print "Replacing all values"
print(defval(5,6,"bye"))

print "Replacing B and C values"
print(defval(5,6))

print "Replacing Only First value"
print(defval(5))

print "   "
def keyargs(a,b,c):
    return a+b-c

print "KEY Arguments"

print keyargs(12,4,18)
print keyargs(b=13,c=9,a=4)
print keyargs(12,b=9,c=2)

print "   "
print "Format changes"

def formatcng(bg='wh', fc='bk', fs=12, ft='TNR' ):
    print ("fs  is",fs)
    print ("ft  is",ft)
    print ("fc  is",fc)
    print ("bg  is",bg)
    
formatcng()
formatcng(fs=16)

print "   "
print "Passing Many Arguments or Values"
def vargs(*args):
    print(args)
    
vargs(12,2,43)
vargs('u','g')


print "   "
print "Putting Default arguments in many arguments "

def vkargs(*args,**kwargs):
    print ("Positional parameter are:-",args)
    print ("Keyword arguments are:-",kwargs)
    print "   "
    
print("With only pp")
vkargs(5,6,7)
print("With only Keywords")
vkargs(u=8,v=9)
print("With mixed")
vkargs('a','b',c=9,d=10)

print "   "

print " Function with Function  "

def square(x):
    return x*x
def applier(q,x):
    return q(x)
print("Square is:-", applier(square,7) )

def rectangle(x,y):
    return 2*(x+y)
def applier(q,x,y):
    return q(x,y)
print("Rectangle is:-", applier(rectangle,2,3) )



























