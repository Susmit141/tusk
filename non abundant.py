# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:28:16 2019

@author: SUSHMIT
"""

def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n
print(is_abundant(12))
print(is_abundant(13))