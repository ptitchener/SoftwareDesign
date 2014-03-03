# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:16:31 2014

@author: paul
"""

def complementary(a):
    """ Returns the complementary DNA pair for an imput of a single letter string
        a: A DNA letter ATGC 
        returns: Complementary dna pair. 
    """
    if type(a)!=str:
        print('Input must be string')
        return
    a = a.upper()
    if a == 'A':
        return 'T'
    elif a == 'T':
        return 'A'
    elif a == 'C':
        return 'G'
    elif a == 'G':
        return 'C'
    else:
        print('Error: Input must be in DNA code')
    
            
        