# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:28:39 2019

@author: Lenovo
"""

N=int(input())
S=0
i=0
while i<N:
    x=int(input())
    S=S+x
    i=i+1
if (48-S)<=(15-N)*10:
    print(int((47-S)/(15-N)+1))
else:
    print("gg")
    