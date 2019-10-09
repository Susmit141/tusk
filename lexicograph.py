# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:44:39 2019

@author: SUSHMIT
"""

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))
