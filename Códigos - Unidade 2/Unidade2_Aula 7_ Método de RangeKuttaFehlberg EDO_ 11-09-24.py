# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:40:11 2024

@author: Luellen

-- Método de Range Kutta Fehlberg --
"""

import numpy as np
import matplotlib.pyplot as plt

def met_rangekuttafeh(fun,x,y):  #x de onde vai integrar #y pode ser um array se tiver multiplas equações
    #a propria equação diferencial já é a derivada
    #xo é um vetor com dois elementos, que diz onde deve começar e onde deve terminar
    #yo é o calor da [] , ou seja é o valor inicial de cada equação diferencial , para várias equações vário yo
    m = np.size(y) #ler o tamanho de y
    n = 1000 #vamos calcular mil pontos
    h = (x[1]-x[0])/n
    
    #dois vetores que vamos guardar a solução
    xplot = np.zeros((n+1,1)) 
    yplot = np.zeros((n+1,m)) #deve ter o números de passos +1
    #cada coluna será a solução de uma equação diferencial diferente
    
    ###
    #Guardando dados iniciais e resolvendo o método
    ###
    y2 = np.zeros((m,1))
    xplot[0] = x[0]
    yplot[0,:] = y
    for i in range(n):
        t = xplot[i,0]
        y2 = yplot[i,:].copy()
        
        k1 = fun(t,y2)
        k2 = fun(t+(h/5), y2+(h/5)*k1)
        k3 = fun(t+(3/10)*h, y2+(3/40)*h*k1+(9/40)*h*k2)
        k4 = fun(t+(3/5)*h, y2+(3/10)*h*k1-(9/10)*h*k2+(6/5)*k3*h)
        k5 = fun(t + h, y2 - (11/54)*h*k1 + (5/2)*h*k2 - (70/27)*k3*h + (35/27)*k4*h)
        k6 = fun(t + (7/8)*h, y2 + (1631/55296)*h*k1 + (175/512)*h*k2 - (575/13824)*k3*h + (44275/110592)*k4*h + (253/4096)*k5*h)
        xplot[i+1,0] = t + h
        for k in range(m):
            yplot[i+1,k] = yplot[i,k] + ((2825/27648)*k1[k]+(18575/48384)*k3[k]+(13525/55296)*k4[k]+(277/14336)*k5[k]+(1/4)*k6[k])*h
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
xplot, yplot = met_rangekuttafeh(derivfuncao, xo, yo)

plt.plot(xplot,yplot,'o')
plt.grid(color = 'k', linestyle = '-', linewidth = 0.1)
plt.legend(['Método de Range Kutta Fehlberg'])
plt.show()

