#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:25:21 2021

@author: ab2018
"""

#find maximum number in list 

number_list = [26, 54, 93, 17, 77, 31, 44, 55, 20]

def mymax(list1):
    max1 = list1[0]
    index = 0
    max_index = 0
    for item in list1 :
        if item > max1 :
            max1 = item  
            max_index = index
            index += 1
    return max1, max_index


for index in range((len(number_list)-1)):
    
    maximum_number, maximum_index = mymax(number_list)
    
    #putting the max number at the end of the list 
    #need the length of the list need a vaiable thats the highest index number
    
    index = len(number_list) -1 
    
    #slice and save as temporary variable
    last_position_value = number_list[index]
    
    #write the maximum number into the last positon
    number_list[index] = maximum_number
    #put the value from last position into the place that was left
    number_list[maximum_index] = last_position_value
    print(number_list)
    
    
    
    
    #want to swap the numbers int eh list and do this in loop 
    #need to make sure that this is alogn the leng of the index 
    
    #lenght number of list is the number of things in the list 
    # last positon is what is occuping the last position of the list 


print(number_list)
    
    
    
    