#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that returns the complement of a sequence, and then reverses the sequence of a user supplied sequence
Created on Mon Jan 25 14:09:06 2021

@author: Bjorn1
"""
#Exercise1
def complement_base(base):
    output = None
    if base == "A":
        output = "T"
    elif base == "G":
        output = "C"
    elif base == "C":
        output = "G"
    elif base == "T":
        output = "A"
    else:
        output = "*"
    return output

def reverse_complement(seq):
    rev_seq = ''
    for base in reverse_string(seq):
        rev_seq += complement_base(base)
    return rev_seq
        
  

        
#Exercise 2 - Write a function to reverse a string, this is the same (custom-made) as putting reversed(seq)
def reverse_string(sequ):
    last_position = len(sequ) - 1
    output = ""
    for i in range(last_position, -1, -1):
        output += sequ[i]
    return output


reverse_complement("AAAATTXTTTTT")      

#Exercise 3













