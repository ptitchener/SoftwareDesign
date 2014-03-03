# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:39:33 2014

@author: paul
"""
from swampy.TurtleWorld import *

def my_square(lower,size):
    if len(lower) != 2:
        raise Exception("First input must be a lower coordinate")
    world = TurtleWorld()
    bob = Turtle()
    bob.x = lower[0]
    bob.y = lower[1]
    i = 0
    for i in range(4):
        fd(bob,size)
        lt(bob)
        
def my_regular_polygon(ll,size,num):
    if len(ll) != 2:
        raise Exception("First input must be a lower coordinate")
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = .001
    bob.x = ll[0]
    bob.y = ll[1]
    iAngle = 360/float(num)
    for i in range(num):
        fd(bob,size)
        lt(bob,iAngle)
        
def my_circle(center,radius):
    if len(center) != 2:
        raise Exception("First input must be a lower coordinate")
    #world = TurtleWorld()
    #bob = Turtle()
    ll = []
    ll.append(center[0])
    ll.append(center[1]-radius)
    n = 500
    side_length = 2*3.14159*radius/n
    my_regular_polygon(ll,side_length,n)
    
def snow_flake_side(turtle,l,level):
    
    if level == 1:
        fd(turtle,l/3)
        lt(turtle,60)
        fd(turtle,l/3)
        lt(turtle,-120)
        fd(turtle,l/3)
        lt(turtle,60)
        fd(turtle,l/3)
    else:
        snow_flake_side(turtle,float(l)/3,level-1)
        lt(turtle,60)
        snow_flake_side(turtle,float(l)/3,level-1)
        lt(turtle,-120)
        snow_flake_side(turtle,float(l)/3,level-1)
        lt(turtle,60)
        snow_flake_side(turtle,float(l)/3,level-1)
    
def snow_flake(turtle,l,level):
    bob.x = 0
    bob.y = -300
    for i in range(6):
        snow_flake_side(turtle,l,level)
        lt(turtle,60)
        i = i+1
    

def recursive_tree(turtle, branch_length, level):
    """ Draw a tree with branch length branch_length and recursion depth of level """
    if level == 1:  
        fd(turtle,branch_length)
        turtle_base = clone_turtle(turtle)
        lt(turtle_base,30)
        fd(turtle_base, branch_length*.6)
        turtle_base.undraw()
        lt(turtle,180)
        fd(turtle,branch_length/3)
        lt(turtle,180-50)
        turtle3 = clone_turtle(turtle)
        fd(turtle3,branch_length)
        turtle3.undraw()
    else:
        fd(turtle,branch_length)
        turtle_base = clone_turtle(turtle)
        lt(turtle_base,30)
        recursive_tree(turtle_base,branch_length*.6,level-1)
        turtle_base.undraw()
        bk(turtle,branch_length/3)
        lt(turtle,-50)
        turtle3 = clone_turtle(turtle)
        recursive_tree(turtle3,branch_length*.6,level-1)
        turtle3.undraw()
        """
        recursive_tree(turtle,branch_length*.6,level-1)
        turtle2 = clone_turtle(turtle)
        lt(turtle2,30)
        recursive_tree(turtle2,branch_length*.6,level-1)
        turtle2.undraw
        lt(turtle,180)
        fd(turtle,branch_length*.6/3)
        lt(turtle,180-50)
        turtle4 = clone_turtle(turtle)
        recursive_tree(turtle4,branch_length*.6,level-1)
        turtle4.undraw
        """

def clone_turtle(turtle):
    turtle2 = Turtle()
    turtle2.x = turtle.x
    turtle2.y = turtle.y
    turtle2.heading = turtle.heading
    return turtle2
    
    
if __name__ == '__main__':
    #my_square([-50,-50],100)
    #my_regular_polygon([-50,-50],30,10)
    #my_circle([0,0],30)
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = .001
    #snow_flake(bob,200,4)
    recursive_tree(bob,100,12)
    bob.undraw()
    wait_for_user()