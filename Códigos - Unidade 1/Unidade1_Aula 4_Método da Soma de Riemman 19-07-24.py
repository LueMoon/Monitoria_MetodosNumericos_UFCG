# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:07:50 2024

@author: Luellen
------ Soma de Riemman ------
"""

def somariemman(fun,a,b):
    n = 10000
    x = (b-a)/n #para o professor x=h
    soma = 0
    for i in range(n): #para ir de 0 a n-1
        soma = soma + fun(a+i*x+(x/2))
    Area = soma * x
    return print(Area)
    
def testefunc(x):
    return x**2

teste = somariemman(testefunc,2,5)