# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:04:47 2019

@author: john
"""

def myfun(x,y):
    ''' myfun(int,int) ->int does some maths operation '''
    global a
    print('x is:' ,x, 'y is:',y)
    a = 8.9/x + 1.2*y
    b = 2.14*x + 7.6/y
    print('a is:' ,a, 'b is:',b)
    z=a+b       #Local Variable
    print (z)

a,b = 5,6
#ret =myfun(a,b)
#print ("Return value is:",ret)
myfun(a,b)
print('a is:' ,a, 'b is:',b)
print(myfun.__doc__)