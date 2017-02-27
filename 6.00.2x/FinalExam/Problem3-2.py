# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:53:50 2016

@author: lantao
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    def draw_one_trial():
        bucket = ['R', 'R', 'R', 'G', 'G', 'G']
        index1 = random.randint(0,5)
        index2 = random.randint(0,4)
        index3 = random.randint(0,3)
        
        ball1 = bucket[index1]
        del bucket[index1]
        
        ball2 = bucket[index2]
        del bucket[index2]
        
        ball3 = bucket[index3]
        del bucket[index3]
        
        if ball1 == ball2 == ball3:
            return True
    
    successes = 0.00
    for trial in range(numTrials):
        if draw_one_trial() == True:
            successes += 1
    
    return successes/numTrials
    