# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:04:12 2024

@Luellen

--- Resolução de sistema linear: Método de Gauss Seidel ---

"""

import numpy as np

def sis_l_GaussSeidel(A,B,xo):#lembre que A e B devem ser matrizes quadradas e xo é estimatica inicial
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
    
    xoo = np.copy(x)
    
    while True:
        for i in range(n):
            soma = 0.0
            #vamos alterar daqui em diante
            for j in range(n): 
                if j > i:
                    soma += A[i,j]*xoo[j]
                elif j < i:
                    soma += A[i,j] * x[j] #x2 é o x da iteração anterior
            x[i] = (B[i] - soma)/A[i,i]
    
        erro = np.max(np.abs(x-xoo))
        if erro < tol:
            return print('O valor é',x, 'fizemos', interx, 'interações')
        if interx > intermax:
            return print('Atingimos o número máximo de interações! Não convergiu')
        
        interx += + 1
        
        xoo = np.copy(x)

a = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
b = np.array([7.85,-19.3,71.4])
xo = np.array([0.0,0.0,0.0])

teste = sis_l_GaussSeidel(a,b,xo)
print(teste)