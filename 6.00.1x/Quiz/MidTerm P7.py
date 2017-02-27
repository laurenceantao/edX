# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:06:08 2016

@author: lantao
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    most = max(max(d1.keys()), max(d2.keys()))
    for i in range(most):
        if d1[i] and d2[i]:
            intersect[i] = f(d1[i], d2[i])
        else:
            difference[i] = f(d1[i], d2[i])
    return (intersect, difference)