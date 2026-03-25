import numpy as np

def matrix_trace(A):
    sum=0
    for i in range (0,len(A)):
        sum+= A[i][i]
    return sum