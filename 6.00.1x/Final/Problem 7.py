# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:55:00 2016

@author: lantao
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """  
    max_power = len(L)-1
    def use_base(x):
        total = 0
        base = x
        for i in range(len(L)):
            power = max_power - i
            element = L[i]*base**power
            total += element
        return total
    return use_base