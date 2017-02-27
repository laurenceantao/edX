# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:11:01 2016

@author: lantao
"""

s = 'who the hell am i?'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1

print('Number of vowels: ' + str(numVowels))