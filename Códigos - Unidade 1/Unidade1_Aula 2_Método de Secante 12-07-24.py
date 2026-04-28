# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:23:30 2024

@author: Luellen
-----------Método da Secante-----------
Método direto de calcular raizes (Forma direta: não necessita de derivada)

"""

from math import exp 

def msecante(fun,x0,x1):
    #teste para saber se há raizes reais
    tol = (1*10**(-6)) #tolerância    
    #criterios de parada
    intermax = 500 #numero maximo de interações
    interx = 0#variavel de contagem
    while True: #enquanto for verdade
        f0 = fun(x0)
        f1 = fun(x1)
        x2 = x1 -(((x1-x0) * f1)/(f1 - f0))
        #Verificações
        if interx > intermax:
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (abs((x2-x1)/x2)<tol):
            return print('O valor convergiu para: ', x2, 'fizemos', interx, 'interações')
        x0 = x1
        x1 = x2
        interx = interx + 1 #contador)

def testefunc(x):
    a = (x-5)*(x+8)
    return a

teste = msecante(testefunc,-1,9)
        
        