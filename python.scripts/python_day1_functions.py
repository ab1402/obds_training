#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:36:14 2021

@author: ab2018
"""

#python functions obds course week 2 day one 
        
        
def complement_base(base):
    """ Returns the watson crick complement"""
    
    if base in 'Aa' :
        return 'T'
    elif base in 'Tt' :
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        print("unknown base")



#for reverse complemetn 
def reverse_complement(seq):
    
    rev_seq = ''
    
    for base in reversed(seq):
        rev_seq += complement_base(base)
    return rev_seq
    
reverse_complement("AAAACCCGGT")                  


#for putting the input character in reverse order not doing complement reverse

def reverse_string(base):
    last_position = len(base) -1
    output = ""
    for i in range(last_position, -1, -1):
        output += base[i]
    return output 

reverse_string("AAAACCCGGT")



if __name__ == "__main__":
    print(reverse_complement("AAAACCCGGT"))
