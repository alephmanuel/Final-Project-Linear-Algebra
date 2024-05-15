"""
Student Name: Aleph M. Gonzalez Pagan
Student Number: 840-20-8993
Student Course: CCOM4065-LD0 - Linear Algebra
--------------------------------------Final Project: Gauss-Jacobi Implementation---------------------------------------------------
"""

import numpy as np

def gauss_jacobi(A, b, x0, max_error, max_iterations):
    n = len(A)
    x = np.copy(x0)
    iteration = 0
    error = np.zeros(n)
    while True:
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_ = np.dot(A[i], x)
            sum_ -= A[i][i] * x[i]
            x_new[i] = (b[i] - sum_) / A[i][i]
        
        error = np.max(np.abs((x_new - x) / x_new))        
        x = np.copy(x_new)
        iteration += 1
        if error <= max_error and iteration >= max_iterations:
            break
    return x, error, iteration
