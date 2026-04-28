""".
Created on Wed Jul 10 14:03:02 2024 *

@author: ALUNO01MM2

-----Método de Newton-----

"""
from math import exp 

def newton(fun,x0):
    tol = (1*10**(-6)) #tolerância    
    #criterios de parada
    intermax = 500 #numero maximo de interações
    interx = 0#variavel de contagem
    h = 1*10**(-6)
    while True: #enquanto for verdade
        f = fun(x0)
        fh = fun(x0+h)#aproximadamente
        df = (fh-f)/h
        x = x0 - (f/df)
        #Verificações
        if interx > intermax:
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (abs(x-x0)<tol):
            return print('O valor convergiu para: ', x, 'fizemos', interx, 'interações')
        x0 = x
        interx = interx + 1 #contador)

def testefunc(x):
    return -0.10597 + (1.671*10**(-4))*x + (9.7215*10**(-8))*(x**2) - (9.5838 * 10**(-11))*(x**3) + (1.9520*10**(-14))*(x**4)

teste = newton(testefunc,1)
        
        