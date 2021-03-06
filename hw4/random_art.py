# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: ptitchener
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import sin
from math import cos
from math import pi

def build_random_function(min_depth, max_depth):
    """This function recursively generates a nested list that represents a function.
    The function is composed of the elements:
        sin_pi
        cos_pi
        product
        square
        squareroot(absolute value)
        x
        y
    
    Inputs:
        min depth: minium level of function commposition
        max depth: maximum level of function commposition
    
    Outputs:
        A nested list that represents a function. The list is composed as:
            sin(pi*x) = [sin_pi,[x]]
            x*y = [prod,[x],[y]]
            and so forth. These functions are composed together. The function evaluate_random_function can read this output
    
    
    """

    if max_depth == 0: #select terminal funcdtions if base case has been reached
        arg = 0
    elif min_depth <= 0: #chose from all fucntions if between the min case and the base case
        arg = randint(0,4) #0 through 4 is used to control the relative liklihood of a product or a single arguement function. This affects the final art
    else: # choose from non-terminal functions if neither case has been reached
        arg = randint(1,4)
    if arg == 0:
        funcs = ['x','y']
        argrand = randint(0,len(funcs)-1)
        return [funcs[argrand]]


    elif arg in [1,2,3]:
        funcs = ['sin_pi','cos_pi','quint','sqrt']
        argrand = randint(0,len(funcs)-1)
        return [funcs[argrand],build_random_function(min_depth-1,max_depth-1)]
    elif arg == 4:
        funcs = ['prod']
        argrand = randint(0,len(funcs)-1)
        return [funcs[argrand], build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]



"""

    if a == 0:
        return ['x']
    elif a == 1:
        return ['y']
    elif a==2:
        return ['prod', build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    elif a==3:
        return ['sin_pi', build_random_function(min_depth-1,max_depth-1)]
    elif a==4:
        return ['cos_pi', build_random_function(min_depth-1,max_depth-1)]
    elif a==5:
        return ['quint',build_random_function(min_depth-1,max_depth-1)]
    elif a ==6:
        return ['sqrt', build_random_function(min_depth-1,max_depth-1)]
"""
        
def evaluate_random_function(f, x, y):
    """ This function will take a nested list "function" (f), and an x and y value to evaluate it at. 
    It returns the value of the fucntion at the point inputed.
    The function must be in the form of a nested list where the list is of the form ['operator',[argument],[argument]]. This list can be as deep as the recursion limit in python allows.
    """
    if f[0] == 'prod': #evalutate product,cos,sin, etc
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == 'sin_pi':
        return sin(pi*evaluate_random_function(f[1],x,y))
    elif f[0] == 'cos_pi':
         return cos(pi*evaluate_random_function(f[1],x,y))
    elif f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y
    elif f[0] == 'quint':
        return (5*evaluate_random_function(f[1],x,y)**4 + 5*(evaluate_random_function(f[1],x,y)**3)  - evaluate_random_function(f[1],x,y)**2 + .2)/5
    elif f[0] == 'sqrt':
        return abs(evaluate_random_function(f[1],x,y))**.5

    else:
        raise Exception("There is a problem with the evaluation function")
        

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
        
        This function also takes the input type and the output type. Use "i" for integers and "f" for floats. This makes it such it can remap a smooth function to list indicies or the like. 
    """
 
    val = float(val)
    input_interval_start = float(input_interval_start)
    input_interval_end = float(input_interval_end)
    output_interval_start = float(output_interval_start)
    output_interval_end = float(output_interval_end)


    input_range = input_interval_end-input_interval_start
    output_range = output_interval_end - output_interval_start
    ratio = output_range/input_range

    return (val - input_interval_start)*ratio + output_interval_start



def the_art_is_the_soul(size):
    """Makes a random piece of art. The input size determines the pixel size of the canvas"""
    min_depth = 4
    max_depth = 6
    
    redFunc = build_random_function(min_depth, max_depth)
    greenFunc = build_random_function(min_depth, max_depth)
    blueFunc = build_random_function(min_depth, max_depth)
    print 'red',redFunc,'green',greenFunc,'blue',blueFunc    
    
    im = Image.new("RGB",(size,size)) #creates a blank image file
    i = 0
    while i in range(size-1): #these loops loop through and fill the image file
        j = 0
        while j in range(size-1):
            #print 'i = ',i,'j=',j
            i_f = float(i)
            j_f = float(j)
            x = remap_interval(i_f, 0, size, -1, 1)#(i_f-size/2)/(size/2) #remaps the interval This was easier than using the remap interval function
            y = remap_interval(j_f, 0, size, -1, 1)
            #print 'x=',x,'y=',y
            r = evaluate_random_function(redFunc, x, y) #evaluating random functions
            g = evaluate_random_function(greenFunc, x, y)
            b = evaluate_random_function(blueFunc, x, y)
            
            r = remap_interval(r,-1,1,0,255)#remaping the evaluation of the random function to a 1 byte color 
            g = remap_interval(g,-1,1,0,255)
            b = remap_interval(b,-1,1,0,255)
            
            
            
            rInt = int(r)  #changing everything into integers before using the color values
            gInt = int(g)
            bInt = int(b)
            im.putpixel((i,j),(rInt,gInt,bInt)) #set color values
            #im.putpixel((i,j),(255,0,0))

            j = j+1
        i = i+1
    im.save('random.png')
    im.show('random.png')
if __name__ == '__main__':
    a  = build_random_function(5,5)
    print a
    b = evaluate_random_function(a,.2,.5)
    print 'b =', b
    the_art_is_the_soul(350)