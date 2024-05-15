"""
Student Name: Efran X. Vera Sonera
Student Number: 802 20 2308
Student Course: CCOM4065-LD0 - Linear Algebra
--------------------------------------Final Project: Gauss-Seidel Implementation---------------------------------------------------
"""

import numpy as np

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