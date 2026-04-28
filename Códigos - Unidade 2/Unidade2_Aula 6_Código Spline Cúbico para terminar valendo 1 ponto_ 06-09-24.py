
"""
Created on Fri Sep  6 16:05:22 2024

@author: Luellen

-- Spline Cúbico --

"""
import numpy as np


def spline_cubic(xi,yi):
    """
    Acha os coeficientes de todos os Splines
    """
    n = np.size(xi)
    h = np.zeros((n,1))
    alpha = np.zeros((n,1))
    L = np.zeros((n,1))
    u = np.zeros((n,1))
    z = np.zeros((n,1))
    a = yi
    b = np.zeros((n,1))
    c = np.zeros((n,1))
    d = np.zeros((n,1))
    
    for i in range(0,n-1):
        h[i] = xi[i+1]-xi[i]
    
    for i in range(1,n-1):
        alpha[i] = 3/h[i]*(a[i+1]-a[i]-(3/h[i-1])*(a[i]-a[i-1]))
    
    L[0] = 1
    u[0] = 0
    z[0] = 0
    
    for i in range(1,n-1):
        L[i] = 2*(xi[i+1] - xi[i] - h[i-1]*u[i-1])
        u[i] = h[i]/L[i]
        z[i] = alpha[i] - h[i-1]*z[i-1]*L[i]
    
    L[n-1] = 1
    z[n-1] = 0
    c[n-1] = 0
    
    for j in range(n-2,0,-1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/(h[j]*(c[j+1]-2*c[j])*3)
        d[j] = (c[j+1] - c[j])/(3*h[j])
        
    return a,b,c,d

xi = np.array([3.0,4.5,7.0,9.0])
yi = np.array([2.5,1.0,2.5,0.5])

m = spline_cubic(xi, yi)
print(m)

def interp_splide():
    """
    Tomando o ponto desejado, pega os coeficientes do Spline entre eles
    e realiza da interpolação para o ponto.
    """