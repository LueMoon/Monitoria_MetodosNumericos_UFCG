# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:07:14 2024

@author: Luellen

--- Resolução de sistema linear: Método de Jacobi ---

"""

import numpy as np

def sis_l_jacobi(A,B,xo = 0):#lembre que A e B devem ser matrizes quadradas e xo é estimatica inicial
#só quando todas convergiram podemos para o metodo
    n = np.size(A,0)
    #Supondo que o usuario passou xo apropriado
    x = np.copy(xo) #duplica um array
    #x = np.zeros((n,1))
    """
    interx, intermax e tol necessarios para metodos interativos
    """
    interx = 0
    intermax = 1000
    tol = 1*10**(-7)
    
    xoo = np.copy(xo)
    
    while True:
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += A[i,j]*xoo[j]
            x[i] = (B[i] - soma)/A[i,i]
    
        erro = np.max(np.abs(x-xoo))
        if erro < tol:
            return print('O valor é',x, 'fizemos', interx, 'interações')
        if interx>intermax:
            return print('Atingimos o número máximo de interações! Não convergiu')
        
        interx += + 1
        xoo = x

a = np.array([[2,-1,1],[1,2,-1],[1,-1,2]])
b = np.array([-1,6,-3])
xo = np.array([0,0,0])

teste = sis_l_jacobi(a,b,xo)
print(teste)