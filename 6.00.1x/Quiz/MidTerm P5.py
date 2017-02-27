# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:47:40 2016

@author: lantao
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total = 0
    for i in range(len(listA)):
        j = listA[i]*listB[i]
        total += j
    return total