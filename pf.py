# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:20:52 2019

@author: SUSHMIT
"""
n = int(input("enter an integer"))
print("factors are")
i = 1
while(i<=n):
    k = 0
    if(n%i==0):
        j = 1
        while(j<=i):
            if(i%j==0):
                k = k+1
                j = j+1
                if(k==2):
                    print(i)
                    i=i+1
                    