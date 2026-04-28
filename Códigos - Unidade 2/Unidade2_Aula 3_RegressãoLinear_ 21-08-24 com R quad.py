# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:57:30 2024

@author: luell
"""

import numpy as np
import matplotlib.pyplot as plt

def linear_regression(xi, yi):
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
    return (b, a)

def func_teste(a, b, x):
    return a*x + b

def r_squared(y, y_pred):
    ss_total = np.sum((y - np.mean(y))**2)
    ss_res = np.sum((y - y_pred)**2)
    r2 = 1 - (ss_res / ss_total)
    return r2

# Dados
xi = np.array([0, 2, 4, 5])
yi = np.array([2, -4, -9, -10])

# Regressão Linear
(b, a) = linear_regression(xi, yi)   
x = np.arange(-5, 5, 0.1)
y = func_teste(a, b, x)

# Calculando R²
r2 = r_squared(yi, func_teste(a, b, xi))

# Plotagem
plt.plot(xi, yi, 'o', label='Dados Observados')
plt.plot(x, y, linestyle='-', label='Regressão Linear')
plt.grid(color='k', linestyle='-', linewidth=0.1)
plt.legend()

# Adicionando R² no gráfico
plt.text(xi.min() + 4 , yi.max() +2 , f'R² = {r2:.2f}', fontsize=10, verticalalignment='top', horizontalalignment='left')

plt.show()
