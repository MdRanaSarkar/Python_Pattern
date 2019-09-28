#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:35:34 2019

@author: rana
"""
"""
*
***
*****
"""
k=1
a=int(input('second pattern: '))
for i in range(1,a+1): #for row
    for j in range(1,k+1): #looping for star
        print("*",end="") #printing * 
    k=k+2                 #for 1 star ,after 2 increasing 3 star,and then 5 star 
    print(" ")            #outer print for next line
