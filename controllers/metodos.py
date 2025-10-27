import numpy as np

class ResultDetail:
    '''
    Clase para almacenar los detalles del resultado de la solución.
    '''
    def __init__(self, **kwargs):
        '''
        Inicializa los detalles del resultado.

        Parámetros opcionales:
        - metodo (str): El método utilizado (e.g., "Gauss-Seidel", "Jacobi").
        - execution_time (float): Tiempo de ejecución en segundos.
        - total_iterations (int): Número total de iteraciones realizadas.
        - converged (bool): Indica si el método convergió o no.
        '''
        self.metodo = kwargs.get("metodo", "")
        self.execution_time = kwargs.get("execution_time", 0.0)
        self.total_iterations = kwargs.get("total_iterations", 0)
        self.converged = kwargs.get("converged", False)

    # Setters and getters can be added as needed
    def set_metodo(self, metodo):
        self.metodo = metodo

    def get_metodo(self):
        return self.metodo

    def set_execution_time(self, execution_time):
        self.execution_time = execution_time

    def get_execution_time(self):
        return self.execution_time

    def set_total_iterations(self, total_iterations):
        self.total_iterations = total_iterations

    def get_total_iterations(self):
        return self.total_iterations

    def set_converged(self, converged):
        self.converged = converged

    def get_converged(self):
        return self.converged
    
    def to_dict(self):
        return {
            "metodo": self.metodo,
            "execution_time": self.execution_time,
            "total_iterations": self.total_iterations,
            "converged": self.converged
        }
    
    def __str__(self):
        return str(self.to_dict())
    
    def __repr__(self):
        return self.__str__()

class ResultHandler:
    def __init__(self):
        self.results = []

    def set_results(self, results):
        self.results = results

    def add_result(self, result):
        self.results.append(result)

    def get_results(self):
        return self.results
    
    def get_result(self, index):
        if index < 0 or index >= len(self.results):
            return None
        return self.results[index]
    
    def clear_results(self):
        self.results = []

    def change_a_result(self, index, new_result):
        if index < 0 or index >= len(self.results):
            return False
        self.results[index] = new_result

        return True
    
    def pop_result(self):
        if len(self.results) == 0:
            return None
        return self.results.pop()
    
    def push_result(self, result):
        self.results.append(result)

    def size(self):
        return len(self.results)
    
# interfaz para el metodo update_from_result_register
class ResultInterfaceRegister:
    def update_from_result_register(self):
        '''
        Metodo para actualizar la interfaz desde el registro de resultados.

        Parámetros:
        - result_register (ResultRegister): El registro de resultados desde el cual actualizar.
        '''
        raise NotImplementedError("Este método debe ser implementado por la subclase.")
    
class ResultRegister:
    def __init__(self, result_handler: ResultHandler, result_detail: ResultDetail, **kwargs):
        '''
        Clase para registrar los detalles del resultado de la solución.

        Parámetros (kwargs):
        - metodo (str): Nombre del método utilizado.
        - execution_time (float): Tiempo de ejecución en segundos.
        - total_iterations (int): Número total de iteraciones realizadas.
        - converged (bool): Indica si el método convergió o no.
        '''
        self.result_handler = result_handler
        self.result_detail = result_detail

        self.page : list[ResultInterfaceRegister] = []

    def register_page(self, page: ResultInterfaceRegister):
        self.page.append(page)

    def unregister_page(self):
        if len(self.page) == 0:
            return None
        
        return self.page.pop()
    
    def new_result_detail(self, result_detail: ResultDetail):
        self.result_detail = result_detail

    def new_result_handler(self, result_handler: ResultHandler):
        self.result_handler = result_handler

    def get_result_detail(self):
        return self.result_detail
    
    def get_result_handler(self):
        return self.result_handler
    
    def notify(self):
        for p in self.page:
            p.update_from_result_register()

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