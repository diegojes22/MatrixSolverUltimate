import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iterations=1000):
    """
    Solve the linear system Ax = b using the Jacobi iterative method.

    Parameters:
    A : 2D array-like
        Coefficient matrix.
    b : 1D array-like
        Right-hand side vector.
    x0 : 1D array-like, optional
        Initial guess for the solution. If None, a zero vector is used.
    tol : float, optional
        Tolerance for convergence. Default is 1e-10.
    max_iterations : int, optional
        Maximum number of iterations. Default is 1000.

    Returns:
    x : 1D array
        Approximate solution vector.
    """
    

    A = np.array(A)
    b = np.array(b)
    n = len(b)

    if x0 is None:
        x0 = np.zeros(n)

    x = np.copy(x0)

    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_ax) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new

        x = x_new

    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=1000):
    """
    Solve the linear system Ax = b using the Gauss-Seidel iterative method.

    Parameters:
    A : 2D array-like
        Coefficient matrix.
    b : 1D array-like
        Right-hand side vector.
    x0 : 1D array-like, optional
        Initial guess for the solution. If None, a zero vector is used.
    tol : float, optional
        Tolerance for convergence. Default is 1e-10.
    max_iterations : int, optional
        Maximum number of iterations. Default is 1000.

    Returns:
    x : 1D array
        Approximate solution vector.
    """
    A = np.array(A)
    b = np.array(b)
    n = len(b)

    if x0 is None:
        x0 = np.zeros(n)

    x = np.copy(x0)

    for iteration in range(max_iterations):
        x_old = np.copy(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x

    raise ValueError("Gauss-Seidel method did not converge within the maximum number of iterations")