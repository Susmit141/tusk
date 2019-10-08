# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 06:39:08 2019

@author: SUSHMIT
"""

def problem_22():
    import csv
    x = list(csv.reader(open('Data22.csv'), delimiter=','))[0]
    x.sort()
    s=0
    for i in range(0,len(x)):
        c=0
        for t in x[i]:
            c+=(ord(t)-64)
        s+=c*(i+1)
    return s