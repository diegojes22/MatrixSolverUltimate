import numpy as np

def jacobi(A, b, tol=1e-10, max_iter=1000):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales Ax = b
    
    Parámetros:
    -----------
    A : array_like
        Matriz de coeficientes (n x n)
    b : array_like
        Vector de términos independientes (n)
    tol : float, opcional
        Tolerancia para el criterio de convergencia (default: 1e-10)
    max_iter : int, opcional
        Número máximo de iteraciones (default: 1000)
    
    Retorna:
    --------
    x : ndarray
        Vector solución
    iter_count : int
        Número de iteraciones realizadas
    converged : bool
        True si el método convergió, False en caso contrario
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    # Vector inicial (ceros)
    x = np.zeros(n)
    x_new = np.zeros(n)
    
    for iter_count in range(max_iter):
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x_new[i] = (b[i] - suma) / A[i, i]
        
        # Verificar convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iter_count + 1, True
        
        x = x_new.copy()
    
    return x, max_iter, False


def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    """
    Método de Gauss-Seidel para resolver sistemas de ecuaciones lineales Ax = b
    
    Parámetros:
    -----------
    A : array_like
        Matriz de coeficientes (n x n)
    b : array_like
        Vector de términos independientes (n)
    tol : float, opcional
        Tolerancia para el criterio de convergencia (default: 1e-10)
    max_iter : int, opcional
        Número máximo de iteraciones (default: 1000)
    
    Retorna:
    --------
    x : ndarray
        Vector solución
    iter_count : int
        Número de iteraciones realizadas
    converged : bool
        True si el método convergió, False en caso contrario
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    # Vector inicial (ceros)
    x = np.zeros(n)
    x_old = np.zeros(n)
    
    for iter_count in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x[i] = (b[i] - suma) / A[i, i]
        
        # Verificar convergencia
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iter_count + 1, True
    
    return x, max_iter, False


# Ejemplo de uso
if __name__ == "__main__":
    # Sistema de ecuaciones de ejemplo
    # 4x + y + z = 7
    # x + 5y - z = 10
    # x + y + 3z = 6
    
    A = np.array([[4, 1, 1],
                  [1, 5, -1],
                  [1, 1, 3]], dtype=float)
    
    b = np.array([7, 10, 6], dtype=float)
    
    print("Sistema de ecuaciones:")
    print("A =")
    print(A)
    print("\nb =", b)
    print("\n" + "="*60)
    
    # Método de Jacobi
    print("\nMÉTODO DE JACOBI")
    x_jacobi, iter_jacobi, conv_jacobi = jacobi(A, b, tol=1e-6, max_iter=100)
    print(f"Solución: {x_jacobi}")
    print(f"Iteraciones: {iter_jacobi}")
    print(f"Convergió: {conv_jacobi}")
    print(f"Verificación Ax = {A @ x_jacobi}")
    
    print("\n" + "="*60)
    
    # Método de Gauss-Seidel
    print("\nMÉTODO DE GAUSS-SEIDEL")
    x_gs, iter_gs, conv_gs = gauss_seidel(A, b, tol=1e-6, max_iter=100)
    print(f"Solución: {x_gs}")
    print(f"Iteraciones: {iter_gs}")
    print(f"Convergió: {conv_gs}")
    print(f"Verificación Ax = {A @ x_gs}")