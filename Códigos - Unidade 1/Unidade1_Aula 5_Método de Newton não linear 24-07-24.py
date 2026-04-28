# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:04:23 2024

@author: Luellen
--- Método de Newton para sistemas não-lineares ---
"""
import numpy as np

def newton_sisnaolinear(fun,x0): #para nosso caso agora x0 é um vetor
    tol = (1*10**(-6)) #tolerância    
    #criterios de parada
    intermax = 500 #numero maximo de interações
    interx = 0#variavel de contagem
    while True:
        J = derivparcial_jacobiana(fun,x0)
        F = fun(x0)
        x = x0 - np.matmul(np.linalg.inv(J),F) #multiplicação de matrizes
        #Verificações
        if interx > intermax:
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (((abs(x-x0)<tol)).all()): #só quando erssa vericação para essas variaveis forem true e vai retornar true
            return print('O valor convergiu para: ', x, 'fizemos', interx, 'interações')
        x0 = x.copy()
        interx = interx + 1 #contador


def derivparcial_jacobiana(fun,x): #a função e o ponto onde desejamo calcular a jacobiana
    J = np.zeros((3,3))
    h = 1*10**(-6)
    for j in range(3):
        f = fun(x)
        x[j] = x[j]+h
        fh = fun(x)
        df = (fh - f)/h
        for i in range(3):
            J[i,j] = df[i]
        x[j] = x[j]-h
    return J
                
def funcao(x_negrito_vetor):
    f = np.zeros((3,1)) #criando um vetor f com tres linhas e uma coluna
    f[0]= 3*x_negrito_vetor[0] - np.cos(x_negrito_vetor[1]*x_negrito_vetor[2]) - (1/2)#colchetes para pegar os elementos do vetor
    f[1] = x_negrito_vetor[0]**(2) - 81*(x_negrito_vetor[1] + 0.1)**(2) + np.sin(x_negrito_vetor[2]) + 1.06
    f[2] = np.exp(-x_negrito_vetor[0] * x_negrito_vetor[1]) + 20* x_negrito_vetor[2] + (10* np.pi - 3)/3
    return f
 

x0 = np.zeros((3,1))
x0[0] = 0.1
x0[1] = 0.1
x0[2] = -0.1
teste = newton_sisnaolinear(funcao,x0)


    