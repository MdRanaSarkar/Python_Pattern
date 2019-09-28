#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 03:41:55 2019

@author: rana
"""
"""
when n=4
   *
  **
 ***
****
"""
"""
It is the same as pattern 3 except only use extra space in line number 21
"""
n=int(input("Take the value of n :")) #for taking input
for i in range(1,n+1): #for row looping 
    for j in range(1,(n+1)-i): #looping both side of star spacing
        print(" ",end=" ")    #printing loop
    for k in range(i):    #looping for printing star
        print("*",end=" ") #print star
    print(" ")