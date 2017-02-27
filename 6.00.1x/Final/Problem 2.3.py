# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:12:28 2016

@author: lantao
"""
balance = 3200000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
annualCompoundRate = (1 + monthlyInterestRate)**12
monthlyPaymentUpper = (balance * annualCompoundRate)/12.0
monthlyPaymentLower = balance/12
monthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower)/2.0
yearlyBalance = balance
for month in range (0,12):
    unpaidBalance = yearlyBalance - monthlyPayment
    yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
while yearlyBalance != 0:
    yearlyBalance = balance
    if yearlyBalance > 0:
        monthlyPaymentUpper = monthlyPayment
    else:
        monthlyPaymentLower = monthlyPayment
        monthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower)/2.0
for month in range (0,12):
    unpaidBalance = yearlyBalance - monthlyPayment
    yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance    
print("Lowest Payment:", str(round(monthlyPayment,2)))