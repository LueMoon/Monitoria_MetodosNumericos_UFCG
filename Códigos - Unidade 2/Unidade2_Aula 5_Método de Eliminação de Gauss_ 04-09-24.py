# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:12:43 2024

@author: Luellen

--- Eliminação de Gauss ---

"""

import numpy as np

def eliminacao_Gauss(A,b):
    n = np.size(b)
    Ax = np.zeros((n,n+1))
    x = np.zeros((n,1))
    #Diagonaliza a matriz (transformar a matriz em uma diagonal superior)
    for i in range(n):
        for j in range(n):
            Ax[i,j] = A[i,j]
    for i in range(n):
        Ax[i,n] = b[i]
    for i in range(0,n-1):
        for j in range(i+1,n):
            m = Ax[j,i]/Ax[i,i]
            for k in range(0,n+1):
                Ax[j,k] = Ax[j,k] - m*Ax[i,k]
                
                
    x[n-1] = Ax[n-1,n]/Ax[n-1,n-1]
    for i in range(n-2,-1,-1):
        soma = 0.0
        for j in range(i+1,n):
            soma += + Ax[i,j]*x[j]
        x[i] = (Ax[i,n] - soma)/Ax[i,i]
    return x
    
A = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
b = np.array([7.85,-19.3,71.4])
x = eliminacao_Gauss(A, b)  
print('\n  Os valores correspondentes a x, y e z são respectivamentes na coluna: ')
print()
print(x)    