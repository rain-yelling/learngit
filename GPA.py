# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:09:40 2019

@author: Lenovo
"""

N=int(input())
GPA=[]
point=[]
i,t,s,a,b,S,S1=0,0,0,0,0,0,0
while i<N:
    x=float(input())
    if x>=60:
        g=4-3*(100-x)**2/1600
    else:
        g=0
    GPA.append(g)
    i=i+1
while t<N:
    h=float(input())
    point.append(h)
    t=t+1
while s<N:
    G=GPA[a]*point[b]
    S+=G
    S1+=point[b]
    a+=1
    b+=1
    s+=1
X=S/S1
print("{:.3f}".format(X))
