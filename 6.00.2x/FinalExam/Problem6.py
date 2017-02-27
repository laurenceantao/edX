# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 19:44:31 2016

@author: lantao
"""

import numpy as np
import itertools

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    choices_sorted = sorted(choices, reverse=True)
    for length in range(0, len(choices_sorted)+1):
        for subset in itertools.combinations(choices_sorted, length):
            subChoice = list(subset)
            if sum(subChoice) == total:
                outputList = []
                for i in range(len(choices)):
                    if choices[i] in subChoice:
                        subChoice.remove(choices[i])
                        outputList.append(1)
                    else:
                        outputList.append(0)
                return np.array(outputList)
    return find_combination(choices, total-1)