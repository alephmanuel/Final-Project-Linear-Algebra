"""
Student Name: Efran X. Vera Sonera
Student Number: 802 20 2308
Student Course: CCOM4065-LD0 - Linear Algebra
--------------------------------------Final Project: Gauss-Seidel Implementation---------------------------------------------------
"""

import numpy as np
import main

def gauss_seidel(A, b, x0, ErrorRMax, MaxIteracion):
    n = len(b)
    x = x0.copy()
    errors = np.zeros(n)
    iterations = 0
    while True:
        x_prev = x.copy()
        for i in range(n):
            sum_ = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (b[i] - sum_) / A[i, i]
            errors[i] = abs((x[i] - x_prev[i]) / x[i])
        ErrorRMax_current = np.max(errors)
        iterations += 1
        if ErrorRMax_current <= ErrorRMax or iterations >= MaxIteracion:
            break
    return x, ErrorRMax_current, iterations


import seidel

def main():
    equaciones = int(input("Ingrese la cantidad de ecuaciones: "))
    variables = int(input("Ingrese la cantidad de variables: "))
    print("Ingrese los coeficientes de las ecuaciones:")
    A = np.zeros((equaciones, variables))
    for i in range(equaciones):
        for j in range(variables):
            A[i, j] = float(input(f"Coeficiente de la variable x{j+1} en la ecuación {i+1}: "))
    b = np.zeros(equaciones)
    for i in range(equaciones):
        b[i] = float(input(f"Constante de la ecuación {i+1}: "))
    ErrorRMax = float(input("Ingrese el error relativo máximo: "))
    MaxIteracion = int(input("Ingrese la cantidad máxima de iteraciones: "))
    x0 = np.zeros(variables)
    for i in range(variables):
        x0[i] = float(input(f"Valor inicial de la variable x{i+1}: "))
    
    print("\nSistema de ecuaciones:")
    for i in range(equaciones):
        equation = " + ".join([f"({A[i, j]} * x{j+1})" for j in range(variables)])
        print(f"Ecuación {i+1}: {equation} = {b[i]}")
    
    opcion = input("Que quieres usar? 1. Seidel, 2. Jacobi ")
    
    if opcion == "1":
        solution, error, iterations = gauss_seidel(A, b, x0, ErrorRMax, MaxIteracion)
        print(f"\nSolución aproximada: {solution}")
        print(f"Error relativo máximo alcanzado: {error}")
        print(f"Total de iteraciones: {iterations}")
    elif opcion == "2":
        #escribe aqui tu llamada de la funcion y el print de los resultados  
        print("Falta lo tuyo capullo")    
    else: 
        print("Opcion no valida")


if __name__ == "__main__":
    main()
