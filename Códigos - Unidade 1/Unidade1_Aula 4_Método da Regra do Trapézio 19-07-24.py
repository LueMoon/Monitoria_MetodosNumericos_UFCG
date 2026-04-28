# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:10:18 2024

@author: Luellen
------ Regra do Trapézio ------
"""

def mtrapezio(fun,a,b):
    n = 100000
    x = (b-a)/n #para o professor x=h
    soma = 0
    fa = fun(a)
    fb = fun(b)
    for i in range(n): #para ir de 0 a n-1
        soma = soma + fun(a+i*x)
    Area = (2*soma + fa + fb)*(x/2)
    return print(Area)
    
def testefunc(x):
    return x**2

teste = mtrapezio(testefunc,2,5)