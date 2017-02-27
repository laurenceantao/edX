# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:12:28 2016

@author: lantao
"""

balance = 3926
annualInterestRate = 0.2
monthlyPayment = 0
yearlyBalance = balance
while yearlyBalance >= 0:
    yearlyBalance = balance
    monthlyPayment += 10
    for month in range (0,12):
        unpaidBalance = yearlyBalance - monthlyPayment
        yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance    
print("Lowest Payment:", str(round(monthlyPayment)))