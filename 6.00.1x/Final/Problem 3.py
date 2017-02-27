# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:32:26 2016

@author: lantao
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if len(us_num) == 1:
        return trans.get(us_num)
    else:
        if us_num[0] == "1":
            tens = "shi"
        else:
            tens = trans.get(us_num[0]) + " shi"
        if us_num[1] == "0":
            units = ""
        else: 
            units = " " + trans.get(us_num[1])
        return tens + units