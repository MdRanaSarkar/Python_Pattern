#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:47:36 2019

@author: rana
"""

a=int(input("take the value : "))

for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    print(" ")