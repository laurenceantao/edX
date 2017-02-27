# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:05:40 2016

@author: lantao
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    import itertools
    max = L[0]
    max_list = []
    for i in range(len(L)):
        for j in range(i,len(L)+1):
            if i == j:
                if L[i] > max:
                    max = L[i]
            else:
                tot = sum(L[i:j])
                if tot > max:
                    max = tot
    return max