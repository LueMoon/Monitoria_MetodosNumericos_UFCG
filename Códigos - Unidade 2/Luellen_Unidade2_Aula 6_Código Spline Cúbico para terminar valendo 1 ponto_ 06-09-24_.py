"""
Created on Mon Sep  9 21:57:25 2024

@author: Luellen
"""
#Importando Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

def spline_cubic(xi, yi): 
    #Essa função vai calcular o spline cúbico entre cada intervalo de dois pontos consecutivos
    """
    Código feito pelo professor Tavernard
    Acha os coeficientes de todos os Splines cúbicos.
    Parâmetros:
    xi : array com os valores de x
    yi : array com os valores de y
    Retorna:
    a, b, c, d : coeficientes dos splines cúbicos para cada intervalo
    """
    n = np.size(xi) #tamanho dos dados 
    h = np.zeros(n-1) #diferença entre pontos consecutivos
    alpha = np.zeros(n-1) 
    L = np.zeros(n)
    u = np.zeros(n)
    z = np.zeros(n)
    a = yi
    b = np.zeros(n-1)
    c = np.zeros(n)
    d = np.zeros(n-1)
    
    for i in range(0, n-1):
        h[i] = xi[i+1] - xi[i] #calcula o intevalo entre os pontos xi
    
    for i in range(1, n-1):
        #calcular a segunda derivada dos splines
        alpha[i] = (3/h[i]) * (a[i+1] - a[i]) - (3/h[i-1]) * (a[i] - a[i-1])
    
    L[0] = 1
    u[0] = 0
    z[0] = 0
    
    for i in range(1, n-1):
        L[i] = 2 * (xi[i+1] - xi[i-1]) - h[i-1] * u[i-1]
        u[i] = h[i] / L[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / L[i]
    
    L[n-1] = 1
    z[n-1] = 0
    c[n-1] = 0
    
    for j in range(n-2, -1, -1):
        c[j] = z[j] - u[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
        
    return a, b, c, d

def interp_spline_c(xi, yi, x):
    """
    Interpola um valor x dado, utilizando os coeficientes da spline cúbica.
    Parâmetros:
    xi : array de valores x
    yi : array de valores y
    x : ponto onde se deseja interpolar
    Retorna:
    y : valor interpolado no ponto x
    """
    # Obter os coeficientes da spline cúbica
    a, b, c, d = spline_cubic(xi, yi)
    
    # Encontrar o intervalo correto para o ponto x
    n = len(xi)
    for i in range(n-1): #i = 0, 1, 2 
        if xi[i] <= x <= xi[i+1]: # 0 <= x <= 3
            # Calcular a interpolação usando os coeficientes
            dx = x - xi[i]
            y = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
            return y
    
        
    return ValueError("Ponto fora do intervalo de interpolação.")

# Função para plotar o gráfico dos splines
def plot_splines(xi, yi):
    # Gerar uma lista de pontos para interpolação (mais densa para suavizar o gráfico)
    x_dense = np.linspace(min(xi), max(xi), 500)
    y_dense = [interp_spline_c(xi, yi, x) for x in x_dense]

    # Plotar os pontos originais
    plt.scatter(xi, yi, color='red', label='Pontos originais')

    # Plotar os splines interpolados
    plt.plot(x_dense, y_dense, label='Spline Cúbico', color='blue')

    # Legendas e título
    plt.title('Interpolação por Spline Cúbico')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso
xi = np.array([3.0, 4.5, 7.0, 9.0])
yi = np.array([2.5, 1.0, 2.5, 0.5])


a = interp_spline_c(xi, yi, 9)
print(a)
b = plot_splines(xi, yi)
