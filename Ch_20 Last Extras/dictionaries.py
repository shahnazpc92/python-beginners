# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:35:13 2019

@author: john
"""

user = {'fn':'JK','uid':197,'ext':209,'pass':'Some_pass','ln':'Kalyan'}
print user
print user['fn']
user['pass']='new_pass'
print user

user.pop('ext')
user['cell']=123456789

print user.keys()

print user.values()

print user.items()

