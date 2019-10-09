# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:56:22 2019

@author: SUSHMIT
"""

def problem_16():
    s=0
    for x in str(2**1000):
        s+=int(x)
    return s
