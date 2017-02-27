# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:31:10 2016

@author: lantao
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    decreasing = [None]
    increasing = [None]
    for i in range(len(L)-1):
        if L[i] < L[i+1]:
            increasing.append(L[i+1])
            decreasing.append(None) 
        elif L[i] == L[i+1]:            
            increasing.append(L[i+1])
            decreasing.append(L[i+1])
        else:
            increasing.append(None)
            decreasing.append(L[i+1])
    
    increase_count = 1
    increase_count_list = []
    for j in range(len(increasing)):
        if increasing[j] is not None:
            increase_count += 1
        else:
            increase_count = 1
        increase_count_list.append(increase_count)

    decrease_count = 1
    decrease_count_list = []
    for k in range(len(decreasing)):
        if decreasing[k] is not None:
            decrease_count += 1
        else:
            decrease_count = 1
        decrease_count_list.append(decrease_count)
        
    max_increase_value = max(increase_count_list)
    max_increase_index = increase_count_list.index(max_increase_value)
    
    max_decrease_value = max(decrease_count_list)
    max_decrease_index = decrease_count_list.index(max_decrease_value)
    
    if max_increase_value > max_decrease_value:
        start_index = max_increase_index - max_increase_value + 1
        end_index = max_increase_index + 1
    elif max_increase_value < max_decrease_value:
        start_index = max_decrease_index - max_decrease_value + 1
        end_index = max_decrease_index + 1
    else:
        if max_increase_index <= max_decrease_index:
            start_index = max_increase_index - max_increase_value + 1
            end_index = max_increase_index + 1
        else:
            start_index = max_decrease_index - max_decrease_value + 1
            end_index = max_decrease_index + 1
    return sum(L[start_index:end_index])