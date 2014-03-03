# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:36:50 2014

@author: paul
"""



def reverse_lookup(d, v):
    """ d - dictionary
    v - value in dictionary"""
    Lout = []
    for k in d:
        if d[k] == v:
            Lout.append(k)
    return Lout


known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

known1 = {}
def Ackermann(m,n):
    if (m,n) in known1:
        return known1[m,n]
    if m == 0:
        res = n+1
    elif m > 0 and n == 0:
        res = Ackermann(m-1,1)
    elif m >0 and n >0:
        res = Ackermann(m-1, Ackermann(m,n-1))             
    known1[m,n] = res
    return res

cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


        
    

if __name__ == "__main__":
    d = {'good1':2,'bad1':5,'good2':2,'bad2':4246,'sasdf':55252}    
    v = 2
    #print reverse_lookup(d,v)
    #print Ackermann(5,3)
    print Ackermann(3, 4)