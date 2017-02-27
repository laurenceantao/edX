# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:41:28 2016

@author: lantao
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    s_remaining = s
    m_sum = 0
    for i in range(len(L)):
        m = int(s_remaining/L[i])
        prod = m* L[i]
        m_sum += m
        s_remaining -= prod
    if s_remaining > 0:
        return "no solution"
    else:
        return m_sum