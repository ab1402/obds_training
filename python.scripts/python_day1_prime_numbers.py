#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:20:54 2021

@author: ab2018
"""

#Print the all the prime numbers under 50

num = 50

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
        
        else:
            print(num, "is a prime number")