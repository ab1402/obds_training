#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:19:56 2021

@author: ab2018
"""
#Accept a number from the user and calculate the sum of all
#numbers between 1 and the given number

num = int(input("enter a number:"))
sum = 0
for num in range(0, num, 1):
    sum = sum+num
print("Sum of first", num, "numbers is:", sum)