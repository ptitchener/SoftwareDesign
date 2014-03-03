# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:31:08 2014

@author: paul
"""


def recursive_flatten(L):
    L1 = []
    for i in range(len(L)):
        if type(L[i])==list:
            L1  = L1 + (recursive_flatten(L[i]))
        else:
           L1.append(L[i])
    return L1
    
def list_count():
    L = []
    text = 'Mary had a little lamb, Little lamb, little lamb, Mary had a little lamb, Its fleece was white as snow And everywhere that Mary went, Mary went, Mary went, Everywhere that Mary went The lamb was sure to go It followed her to school one day School one day, school one day It followed her to school one day Which was against the rules. It made the children laugh and play, Laugh and play, laugh and play, It made the children laugh and play To see a lamb at school'
    i = 0    
    for w in text:
        if L1[i][1] != 



    
if __name__ == '__main__':
    #print recursive_flatten([1,2,[3,4]])
    #print recursive_flatten([1,2,[3,["asdf",4.0]],3])
    print recursive_flatten([1,5,[1,3],5.0,["test","testing"],"blah"])