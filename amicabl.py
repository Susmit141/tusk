# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 06:29:41 2019

@author: SUSHMIT
"""

def problem_21():
    s,i=0,0
    while i <=10000:
        x=sum(Factor(i)[0:-1])
        t=sum(Factor(x)[0:-1])
        if t==i and i!=x:
            s +=(i+x)
            i=x+1
        i+=1
    return s
