# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:45:10 2014

@author: paul
"""
import random

def hinge(n):
    if n<0:
        return 0
    else:
        return n

def print_number_of_days(n):
    if n ==1 :
        print 'Input is 1 day'
    else:
        print 'Input is', n,'days'

def m_min_to_mi_hour(n):
 
    
    n = n*m*m/min
    a = n.asUnit(mile*mile/h)
    return a *60


def has_duplicates(L):
    b = False
    for a in L:      
        if L.count(a) >1:
            b = True
            return b
    return b
        

def birthday():
    dup = 0
    for x in range(1000):
        L1 = []
        for x in range(23):
            L = []
            L.append(random.randint(0,12))
            L.append(random.randint(0,30))
            L1.append(L)
        print L1
        if has_duplicates(L):
            dup = dup+1
    return dup/1000
            
            