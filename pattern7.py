#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:43:34 2019

@author: rana
"""

"""
when n=4
print this:
* * * *
* * *
* *
*
"""
def pyramid(row):
    for i in range(n,0,-1):
        print("* "*(i)+" "*(n-i))
    print()


n= int(input("Take the value: "))
pyramid(n)
        