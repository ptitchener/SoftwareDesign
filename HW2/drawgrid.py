# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/paul/.spyder2/.temp.py

Paul Titchener
1/28/14
"""


def drawgrid1(rows,columns)

    def line1(columns):
        print columns*'+ - - - - ','+' #prints iterated bits of colums
        
    def line2(columns):
        for x in range(0, 4):
            print columns*'|         ','|' #prints iterated bits of column type 2
    
    def drawgrid(rows,columns):
        for x in range(0, rows): #goes through number of rows and prints iterated bits of the entire pattern
            line1(columns)
            line2(columns)
        line1(columns)          #endcap
        
    
    drawgrid(rows,columns)  #two rows/columns