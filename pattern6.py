#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:31:32 2019

@author: rana
"""
"""
when n=4
then 
    *
   * *
  * * *
 * * * *
  * * *
   * *
    *

"""

def pyramid(row):# here call the function
    for i in range(1,row+1): # row checking ro 1 to n star printing
        print(" "*(row-i)+"* "*(i)) # printing  above line 11 to 14                                    """
    for j in range(row-1,0,-1):     # checking inverse row
        print(" "*(row-j)+"* "*(j)) # print line 15 to 17
n=int(input("Take input value: "))
pyramid(n)
