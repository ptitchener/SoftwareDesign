# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:33:47 2014

@author: paul
"""

def sum_of_squares(n):
    x = 0
    sum = 0
    while x in range(n+1):
        sum = sum+x**2
        #print 'sum=', sum 
        #print 'x square=', x**2
        x = x+1
    return sum
    
def filter(L):
    x = 0
    Lout = []
    while x in range(len(L)):
        #print L[x]
        if L[x] > 0:
            Lout.append(L[x])
        x = x+1
    return Lout
    
def sum_of_squares_r(n):
    """finds the sum of squres recursively"""
    if n == 1:
        return 1
    return n**2 + sum_of_squares_r(n-1)
    
def factorial_my(n):
    if n == 1:
        return 1
    return n*factorial_my(n-1)
    
def fib_my(n):
    if n==0:
        return 1
    elif n ==1: 
        return 1
    return fib_my(n-1)+fib_my(n-2)
    
def is_Palindrome(S):
    if len(S)<1:
        #print 'Palindrome'
        return True
    if S[0]==S[len(S)-1]:
        #print S[0]
        b = S[1:len(S)-2]
        a = is_Palindrome(b)
        return a
    else:
        #print 'No'
        return False
        
    
