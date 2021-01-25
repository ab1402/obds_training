#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:19:07 2021

@author: ab2018
"""

#Print the first 10 negative numbers using a for loop


list1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

for num in list1:
    
    if num < 0:
        print(num, end= "")