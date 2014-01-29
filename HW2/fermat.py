# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:18:45 2014

@author: paul
1/28/14
"""

def fermat(a,b,c,n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    if n<=2:
        print 'N must be greater than 2'
    else:
        if a**n + b**n == c**n:
            print 'Holy smokes, Fermat was wrong...which really means my program does not work... :('
        else:
            print 'No, that does not work'
            

        
