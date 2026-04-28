# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:02:14 2024

@author: Luellen 
--- Regressão Linear ---
"""

import numpy as np
import matplotlib.pyplot as plt

def linear_regression(xi,yi):
    n = np.size(xi)
    somaX = 0
    somaY = 0
    somaXY = 0
    somaX2 = 0
    for i in range(n):
        somaX = somaX + xi[i]
        somaY = somaY + yi[i]
        somaXY = somaXY + xi[i]*yi[i]
        somaX2 = (somaX2) + xi[i]**2
    b = (somaX2*somaY - somaX*somaXY)/(n*somaX2 - somaX**2)
    a = (n*somaXY - somaX * somaY)/(n*somaX2 - somaX**2)
    return (b,a)

xi = np.array([0,2,4,5])
yi = np.array([2,-4,-9,-13])

def func_teste(a,b,x):
    return a*x + b

(b,a) = linear_regression(xi, yi)   
x = np.arange(-5,5,0.1)
y = func_teste(a,b,x)

plt.plot(xi,yi,'o')
plt.plot(x,y, linestyle = '-')
plt.grid(color = 'k', linestyle = '-', linewidth = 0.1)
plt.legend(['Regressão Linear'])

    
    