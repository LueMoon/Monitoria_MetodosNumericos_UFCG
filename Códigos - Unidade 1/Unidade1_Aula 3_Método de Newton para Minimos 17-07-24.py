"""
Created on Wed Jul 17 14:12:55 2024

@author: Luellen

----Método de Newton para mínimos----
Queremos achar mínimos e máximos de funções.
Para achar a raiz da derivada da função

"""

from math import exp 

def newton_minimo(fun,x0):
    tol = (1*10**(-8)) #tolerância    
    #criterios de parada
    intermax = 5000 #numero maximo de interações
    interx = 0#variavel de contagem
    h = 1*10**(-6)
    while True: #enquanto for verdade
        fo = fun(x0)
        fh = fun(x0+h)#aproximadamente
        fh2 = fun(x0+(2*h))
        df1 = (fh-fo)/h
        df2 = (fh2-fh)/h
        d2f = (df2-df1)/h
        x = x0 - (df1/d2f)
        #Verificações
        if interx > intermax:
            return print('Não convergiu, ou seja atingiu o limite máximo de interações')
        elif (abs(x-x0)<tol):
            return print('O valor convergiu para: ', x, 'fizemos', interx, 'interações')
        x0 = x
        interx = interx + 1 #contador

def testefunc(x):
    return (2*x)/(4 + 0.8*x + (x**2) + 0.2*(x**(3)))

teste = newton_minimo(testefunc,1)