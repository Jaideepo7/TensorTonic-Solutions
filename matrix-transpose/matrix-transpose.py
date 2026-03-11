import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m = len(A[0])
    n = len(A)
    TA = (np.zeros((m,n)))

    for i in range(m):
        for j in range(n):
            TA[i][j]= A[j][i]

    return TA
