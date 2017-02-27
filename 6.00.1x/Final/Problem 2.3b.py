# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:31:24 2016

@author: lantao
"""

balance = 999999
annualInterestRate = 0.18
epsilon = 0.01
monthlyInterestRate = annualInterestRate/12
annualCompoundRate = (1 + monthlyInterestRate)**12
monthlyPaymentUpper = (balance * annualCompoundRate)/12.0
monthlyPaymentLower = balance/12
monthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower)/2.0
yearlyBalance = balance
for month in range (0,12):
    unpaidBalance = yearlyBalance - monthlyPayment
    yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance 
while abs(yearlyBalance) >= epsilon:
    if yearlyBalance < 0:
        monthlyPaymentUpper = monthlyPayment
        yearlyBalance = balance
        monthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower)/2.0
        for month in range (0,12):
            unpaidBalance = yearlyBalance - monthlyPayment
            yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance 
    else:
        monthlyPaymentLower = monthlyPayment
        yearlyBalance = balance
        monthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower)/2.0
        for month in range (0,12):
            unpaidBalance = yearlyBalance - monthlyPayment
            yearlyBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance 
print("Lowest Payment:", str(round(monthlyPayment,2)))