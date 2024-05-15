"""
Students Name: Aleph M. Gonzalez Pagan & Efran X. Vera Sonera
Student Number: 840-20-8993 & 802-20-2308
Student Course: CCOM4065-LD0 - Linear Algebra
--------------------------------------------------Final Project: Main File---------------------------------------------------------
"""
from Gauss_Seidel import *
from Gauss_Jacobi import *

def main():
    while True:
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
        
        while True:
            opcion = input("Seleccione el Metodo a usar:\n 1. Seidel, 2. Jacobi, 3. Salir\n")
            
            if opcion == "1":
                print("\n Metodo de Gauss-Seidel:")
                solution, error, iterations = gauss_seidel(A, b, x0, ErrorRMax, MaxIteracion)
                print(f"\nSolución aproximada: {solution}")
                print(f"Error relativo máximo alcanzado: {error}")
                print(f"Total de iteraciones: {iterations}")
            elif opcion == "2":
                print("\n Metodo de Gauss-Jacobi:")
                solution, error, iterations = gauss_jacobi(A, b, x0, ErrorRMax, MaxIteracion)
                print(f"\nSolución aproximada: {solution}")
                print(f"Error relativo máximo alcanzado: {error}")
                print(f"Total de iteraciones: {iterations}")
            elif opcion == "3":
                break
            else: 
                print("Opcion no valida, intentelo de nuevo")
        
        while True:
            end_program = input("\nFinalizar Programa (y/n)?")
            if end_program == 'y':
                return
            elif end_program == 'n':
                break
            else:
                print("Opcion no valida, intentelo de nuevo")



if __name__ == "__main__":
    main()
