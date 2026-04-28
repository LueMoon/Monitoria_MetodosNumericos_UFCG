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
    J = np.zeros((5,5))
    h = 1*10**(-6)
    for j in range(5):
        f = fun(x)
        x[j] = x[j]+h
        fh = fun(x)
        df = (fh - f)/h
        for i in range(5):
            J[i,j] = df[i]
        x[j] = x[j]-h
    return J

K1 = 10**(-6.3)
K2 = 10**(-10.3)
Kw = 10**(-14)
Alk = 2e-3
cT = 3e-3
def fun(x): #entra com um array de chutes
    CO2, HCO3, CO3, H, OH = x #Note que são as concentrações de cada espécie
    #Definindo as equações não-lineares
    eq1 = K1 - ((H * HCO3) / CO2  )      # Equação de equilíbrio do CO2 e HCO3⁻ -> primeira dissociação 
    eq2 = K2 - ((H * CO3) / HCO3 )       # Equação de equilíbrio do HCO3⁻ e CO3²⁻ -> segunda dissociação
    eq3 = Kw -( H * OH    )              # Produto iônico da água
    eq4 = cT - (CO2 + HCO3 + CO3)      # Concentração total de carbono inorgânico
    eq5 = Alk - (HCO3 + 2 * CO3 + OH - H)  # Equilíbrio da alcalinidade
    return np.array([eq1,eq2,eq3,eq4,eq5]) #retornando os resultados das equações


# Valores iniciais aproximados
x0 = np.array([1e-3, 1e-3, 1e-5, 1e-7, 1e-7])

# Chamando a função para resolver o sistema
newton_sisnaolinear(fun, x0)

    