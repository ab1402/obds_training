#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:13:15 2021

@author: ab2018
"""

print('hello world')
test = []
print(test,'is',bool(test))


number = 23 
guess = int(input("enter and integer :"))

if guess == number:
    print("Congratulations you guess its.")
    print ('(but you do not win any prizers!)')
    
elif guess < number:
    print("no, it is higher than that")
    
else:
    print ("no it is lower than that")
    

running = True 
while running:
    guess = int(input("enter and integer: "))
    if guess == 20:
        print("Congratulations!")
        
        running = False  
        
    
    elif guess < 20:
        print("no it is higher than that")
        
    else: 
        print("No it is lower than that")
        
integer = 1
print("integer")

string = "how are you ?"

i = 1 
while i <=10 :
    print(i)
    i += 1

list1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

for num in list1:
    
    if num < 0:
        print(num, end= "")
        
num = int(input("enter a number:"))
sum = 0
for num in range(0, num, 1):
    sum = sum+num
print("Sum of first", num, "numbers is:", sum)

num = 50

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
        
        else:
            print(num, "is a prime number")


      
        