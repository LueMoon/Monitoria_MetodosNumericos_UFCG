# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:05:22 2024

@author: Luellen
---- Interpolação de lagrange ----
"""
import numpy as np

def lagrange(xi, yi, x): #x é o ponto que queremos interpolar para receber no final o y
#os vetores de entrada devem ter o mesmo tamanho
    n = xi.size #pega o maior tamanho das n linhas
    l = np.zeros(shape = n) #cria uma matriz quadrada do tamanho n # ou poderiamos ter colocado np.zeros((n,n))
    for k in range(n):
        prod = 1
        for i in range(n):
            if i != k:
                prod = prod*(x-xi[i])/(xi[k]-xi[i])
        l[k] = prod
    soma = 0
    for k in range(n):
        soma = soma + yi[k]*l[k]
    return soma

xi = np.array([2,2.75,4])
yi = np.array([1/2,1/2.75,1/4])
x = 3
y = lagrange(xi, yi, x)
print(y)


