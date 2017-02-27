# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:56:11 2016

@author: lantao
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for month in range (0,12):
    payment = balance * monthlyPaymentRate
    unpaidBalance = balance - payment
    balance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
print("Remaining Balance:", str(round(balance,2)))