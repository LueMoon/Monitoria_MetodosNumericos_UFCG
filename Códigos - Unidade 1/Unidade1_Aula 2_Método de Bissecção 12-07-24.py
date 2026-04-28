# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:49:49 2024

@author: Luellen
-----------Método da Bisecção-----------
Vai divindindo o intervalo ao meio até que o intervalo seja tão pequeno
que consiga descobrir a raiz.
"""


from math import sqrt, log10

def mbisseccao(fun,a,b):
    #teste para saber se há raizes reais
    tol = (1*10**(-6)) #tolerância    
    #criterios de parada
    intermax = 500 #numero maximo de interações
    interx = 0#variavel de contagem 
    while True: #enquanto for verdade
        c = (a+b)/2
        fa = fun(a)
        print(fa)
        fc = fun(c)
        print(fc)
        if fa == 0:
            return print(a)
        elif fc == 0:
            return print(c)
        
        if (fa * fc < 0):
            b = c
        else:
            a = c
        #Verificações
        if (interx > intermax):
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (abs(a-b)<tol):
            return print('O valor convergiu para: ', (a+b)/2 , 'fizemos', interx, 'interações', fa)
        interx = interx + 1 #contador

def testefunc(x):
    f = (1/sqrt(x)) + 2*(log10(((10**(-4))/3.7) + (2.51/((2*10**(5))*sqrt(x)))))
    return f

teste = mbisseccao(testefunc,0.01,1)

        
        