# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:18:11 2014

@author: paul
"""

def imustbegoing(x):
    x = int(x)
    if x <= 100 and x >= 0:
        print 'hello'
    elif x>100 and x<500:
        print 'goodbye'
    elif x>600 and x<1000:
        print 'ciao'
    else:
        print 'use the right values'
"""
x = 200
if x>=0 and x<=100:
    print 'Hello'
elif x>100:
    print 'goodbye'
"""