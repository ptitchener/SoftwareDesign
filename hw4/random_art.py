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
    if max_depth == 0:  #this code determines whether the program has reached the base case or not. 
        base = True
    
    elif min_depth<0:
        c = randint(0,2) #there is a 1/3 chance of stopping at each point between the max and the min depth of recusion
        if c == 1:
            base = True
        else:
            base = False
    else:
        base = False
    """ I see what you're doing here, and it works, but this it's unnecessarily complicated.
        
        if haven't reached min, choose randomly from non terminal functions.
        if between min and max, choose randomly from all functions.
        if max, choose from terminal functions.

        That said, I appreciate the spirit of finding a solution that works."""



    if base: #actions to perform if the base case has been reached. 
        a = randint(0,1)
        if a == 0:
            return ['x']
        elif a == 1:
            return ['y']
        else:
            raise Exception("Randint is not setup properly")
    else: #if the base case has not been reached, continue to compose functions
        b = randint(0,4)
        if b==0:
            return ['prod', build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
        elif b==1:
            return ['sin_pi', build_random_function(min_depth-1,max_depth-1)]
        elif b==2:
            return ['cos_pi', build_random_function(min_depth-1,max_depth-1)]
        elif b==3:
            return ['quint',build_random_function(min_depth-1,max_depth-1)]
        elif b ==4:
            return ['sqrt', build_random_function(min_depth-1,max_depth-1)]

        """ This can be written more cleanly/more generizably by sorting the functions by # of args and doing one elif for each # of args.
            Think about what would happen if you decided you wanted to choose from 50 different functions here... """

        else:
            raise Exception("Randint is not setup properly")
def evaluate_random_function(f, x, y):
    """ This function will take a nested list "function" (f), and an x and y value to evaluate it at. 
    It returns the value of the fucntion at the point inputed.
    The function must be in the form of a nested list where the list is of the form ['operator',[argument],[argument]]. This list can be as deep as the recursion limit in python allows.
    """
    if f[0] == 'prod': #evalutate product,cos,sin, etc
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == 'sin_pi':
        return sin(3.14159*evaluate_random_function(f[1],x,y)) 
        # the math library has a built in pi constant so when you import, if you say 'from math import *' then you can just use 'pi' in the code.  More accurate, more readable.
    elif f[0] == 'cos_pi':
         return cos(3.14159*evaluate_random_function(f[1],x,y))
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
        

def remap_interval(val,input_type, input_interval_start, input_interval_end,output_type, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
        
        This function also takes the input type and the output type. Use "i" for integers and "f" for floats. This makes it such it can remap a smooth function to list indicies or the like. 
    """
    if input_type == 'f':
        lengthIn = input_interval_end - input_interval_start
    elif input_type == 'i':
        lengthIn = input_interval_end - input_interval_start+1
    else:
        raise Exception("Not a valid input type. Valid input types are f: float, and i: int. Integers will calculate as indicies inclusive of the endpoints and floats will calculate normally")

    if output_type == 'f':
        lengthOut = output_interval_end - output_interval_start
    elif output_type == 'i':
        lengthOut = output_interval_end - output_interval_start +1
    else:
        raise Exception("Not a valid output type. Valid input types are f: float, and i: int. Integers will calculate as indicies inclusive of the endpoints and floats will calculate normally")

    
    print 'LengthIn',lengthIn,'length out',lengthOut    
    
    
    valInt1 = float(val)-float(input_interval_start)
    valInt2 = valInt1/lengthIn
    valInt3 = valInt2*lengthOut
    """ You chose to use put these as seperate calculations for a reason.  Choose a variable name that explains the reason.  The 1, 2, 3 is arbitrary. """
    if output_type == 'i':
        return int(valInt3+output_interval_start)
    else:
        return float(valInt3+output_interval_start)

    """ why not just convert them all to floats and do only float math? """

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
            x = (i_f-size/2)/(size/2) #remaps the interval This was easier than using the remap interval function
            y = (j_f-size/2)/(size/2)
            #print 'x=',x,'y=',y
            r = evaluate_random_function(redFunc, x, y) #evaluating random functions
            g = evaluate_random_function(greenFunc, x, y)
            b = evaluate_random_function(blueFunc, x, y)
            
            r = (r+1)*255/2 #remaping the evaluation of the random function to a 1 byte color 
            g = (g+1)*255/2
            b = (b+1)*255/2  

            """this remapping work should be done in the remap_interval funcion."""         
            
            
            
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