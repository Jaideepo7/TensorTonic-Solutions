def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here

    for i in range(steps):
        fx= a*x0*x0 + b*x0+c
        dfx = 2*a*x0 + b
        if dfx == 0:
            return x0
        x0 = x0 - lr*dfx

    return x0