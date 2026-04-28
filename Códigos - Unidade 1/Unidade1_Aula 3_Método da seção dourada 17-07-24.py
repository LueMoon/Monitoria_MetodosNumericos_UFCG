# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:33:18 2024

@author: ALUNO01MM2
---- Minimização Método da seção dourada ----
Usa a seção dourada (Tecnica)
"""

from math import exp 

def secao_dourada(fun,a,b):
    #teste para saber se há raizes reais
    tol = (1*10**(-6)) #tolerância    
    #criterios de parada
    intermax = 500 #numero maximo de interações
    interx = 0#variavel de contagem 
    while True: #enquanto for verdade
        x1 = a + 0.382*(b-a)
        x2 = a + 0.618*(b-a)
        f1 = fun(x1)
        f2 = fun(x2)
        if f1>f2:
            a = x1
            x1 = x2
            x2 = a + b - x1
            f1 = f2
            f2 = fun(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + b - x2
            f2 = f1
            f1 = fun(x1)
        

        #Verificações
        if (interx > intermax):
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (abs(b-a)<tol):
            return print('O valor convergiu para: ', (a+b)/2 , 'fizemos', interx, 'interações')
        interx = interx + 1 #contador)

def testefunc(x):
    f = 100*x - 2*x**2
    return f

teste = secao_dourada(testefunc,-4,7)
        
        