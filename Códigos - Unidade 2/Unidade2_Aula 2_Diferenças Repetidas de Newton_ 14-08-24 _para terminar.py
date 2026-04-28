# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:11:10 2024

@author: ALUNO01MM2
"""

import numpy as np

def diferenca_newton(xi, yi, x): #x é o ponto que queremos interpolar para receber no final o y (conjunto de pontos)
    n = np.size(xi)#pega o maior tamanho das n linhas
    f = np.zeros((n,n)) #cria uma matriz quadrada do tamanho n # ou poderiamos ter colocado np.zeros((n,n))
    for i in range(n):
        f[i,0] = yi[i]
        for i in range(1,n):
            for j in range(1,i+1):
                f[i,j] = (f[i,j-1] - f[i-1,j-1])/(xi[i] - xi[i-j])
    soma = 0
    for i in range(n):
        prod = 1
        for j in range(i):
            prod = prod * (x-xi[j])
        soma = soma + f[i,i]*prod
    return soma

xi = np.array([1,2,3,4,6])
fi = []
for i in range(3):
    a = xi[i]
    f = np.exp(a)
    f.append(fi)
print(fi)
    
    
#yi = np.array([3.6487,6.4817,22.0855,92.0171])
x = 5
y = diferenca_newton(xi, fi, x)
print(y)


