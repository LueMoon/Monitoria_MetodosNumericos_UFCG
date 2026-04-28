# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:15:13 2024

@author: Luellen

--- Interpolação Diferenças divididas ---
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
yi = np.array([np.exp(1),np.exp(2),np.exp(3),np.exp(4),np.exp(6)])
x = 2.5
y = diferenca_newton(xi, yi, x)
print(y)


