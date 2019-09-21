# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 03:34:29 2019

@author: SUSHMIT
"""

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)