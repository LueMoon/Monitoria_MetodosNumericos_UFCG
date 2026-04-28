# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:37:23 2024

@author: Luellen

-- Método de Euler --

"""

import numpy as np
import matplotlib.pyplot as plt

def met_euller(fun,xo,yo): 
    #a propria equação diferencial já é a derivada
    #xo é um vetor com dois elementos, que diz onde deve começar e onde deve terminar
    #yo é o calor da [] , ou seja é o valor inicial de cada equação diferencial , para várias equações vário yo
    n = 1000 #vamos calcular mil pontos
    h = (xo[1]-xo[0])/n
    
    #dois vetores que vamos guardar a solução
    xplot = np.zeros((n+1,1)) 
    yplot = np.zeros((n+1,1)) #deve ter o números de passos +1
    xplot[0,0] = xo[0]
    yplot[0,0] = yo
    
    
    for i in range(n):
        yplot[i+1] = yplot[i] + h*fun(xplot[i],yplot[i])
        xplot[i+1] = xplot[i] + h
    return xplot, yplot

def derivfuncao(t,ca):
    return -0.15*ca

#main
to = np.array([0,100]) #h
ca0 = 5.0
xplot, yplot = met_euller(derivfuncao, to, ca0)

plt.plot(xplot,yplot,'o')
plt.grid(color = 'k', linestyle = '-', linewidth = 0.1)
plt.legend(['Método de Euller'])
plt.show()
    