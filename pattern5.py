#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 03:45:38 2019

@author: rana
"""

"""
when n=4 then create this piramid:
* * * *
 * * *
  * *
   *
"""


def piramid(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print(" ")

a=int(input("Take the n's value: "))
piramid(a)