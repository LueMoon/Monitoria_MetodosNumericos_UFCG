# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:40:11 2024

@author: Luellen

-- Método de Euler para Múltiplas Equações --
"""

import numpy as np
import matplotlib.pyplot as plt

def met_eulermult(fun,x,y):  #x de onde vai integrar #y pode ser um array se tiver multiplas equações
    #a propria equação diferencial já é a derivada
    #xo é um vetor com dois elementos, que diz onde deve começar e onde deve terminar
    #yo é o calor da [] , ou seja é o valor inicial de cada equação diferencial , para várias equações vário yo
    m = np.size(y) #ler o tamanho de y
    n = 4 #vamos calcular mil pontos
    h = 0.5 #(x[1]-x[0])/n
    
    #dois vetores que vamos guardar a solução
    xplot = np.zeros((n+1,1)) 
    yplot = np.zeros((n+1,m)) #deve ter o números de passos +1
    #cada coluna será a solução de uma equação diferencial diferente
    
    ###
    #Guardando dados iniciais e resolvendo o método
    ###
    y2 = np.zeros((m,1))
    xplot[0] = x[0]
    for i in range(m):
        yplot[0,i] = y[i]
    for i in range(n):
        t = xplot[i]
        for k in range(m):
            y2[k] = yplot[i,k]
        f = fun(t,y2)
        xplot[i+1,0] = t + h
        for k in range(m):
            yplot[i+1,k] = yplot[i,k] + h*f[k]
    return xplot,yplot

def derivfuncao(xo,yo):
    dy1 = -0.5*yo[0]
    dy2 = 4 - 0.3*yo[1] - 0.1*yo[0]
    return np.array([dy1,dy2])

#PVI
xo = np.array([0.0,2.0]) #de onde vai integrar #solução em t = 0
yo = np.array([4.0,6.0])# solução em t=0

"""
Lembre que x é uma matriz e y é um vetor!
"""


#chamando o método
xplot, yplot = met_eulermult(derivfuncao, xo, yo)

plt.plot(xplot,yplot,'o')
plt.grid(color = 'k', linestyle = '-', linewidth = 0.1)
plt.legend(['Método de Euler Multiplas Equações'])
plt.show()
    