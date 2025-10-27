from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt

from ui.solver_screen import Ui_solver_screen
from controllers.navigation_controller import NavigationController, RESULT_PAGE_INDEX
from controllers.matrix_controller import MatrixController

from controllers.metodos import gauss_seidel, jacobi, ResultDetail, ResultHandler, ResultInterfaceRegister, ResultRegister
from controllers.result_detail_dialog_controller import ResultDetailDialogController

import time

class SolverPageController(QWidget, Ui_solver_screen, ResultInterfaceRegister):
    """
    Clase controladora que hereda de QWidget y usa la interfaz generada.
    Aquí va toda tu lógica personalizada.
    """

    def __init__(self, navigation_controller : NavigationController, result_register : ResultRegister = None, parent=None):
        super().__init__(parent)
        # Configura la interfaz generada automáticamente
        self.setupUi(self)
        self.navigation_controller : NavigationController = navigation_controller
        self.matrix_controller : MatrixController = MatrixController()
        self.result_register : ResultRegister = result_register
        
        # Conecta los eventos a tus métodos
        self._connect_signals()
        
        # Inicializa variables o estados si es necesario
        self._initialize_data()
    
    def _connect_signals(self):
        """
        Conecta las señales de los widgets a los métodos manejadores.
        """
        self.resolver_btn.clicked.connect(self.on_solve_button_clicked)
        self.limpiar_matriz_btn.clicked.connect(self.on_clear_button_clicked)
        self.matrix_size_slider.valueChanged.connect(self.on_matrix_size_changed)
    
    def _initialize_data(self):
        """
        Inicializa datos o configuraciones adicionales.
        """
        self._config_matriz()

    def _config_matriz(self):
        self.matrix_controller.set_matriz_fields([
            [self.a11_field, self.a12_field, self.a13_field, self.a14_field, self.c1_field],
            [self.a21_field, self.a22_field, self.a23_field, self.a24_field, self.c2_field],
            [self.a31_field, self.a32_field, self.a33_field, self.a34_field, self.c3_field],
            [self.a41_field, self.a42_field, self.a43_field, self.a44_field, self.c4_field],
        ])

    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================
    def on_solve_button_clicked(self):
        """
        Se ejecuta cuando el usuario hace clic en el botón de resolver.
        """
        self._config_matriz()
        self.matrix_controller.print_matriz()
        self.absolute_solver()

    def on_clear_button_clicked(self):
        """
        Se ejecuta cuando el usuario hace clic en el botón de limpiar.
        """
        self.matrix_controller.clear_matriz()
        self.matrix_controller.set_size_to_default()
        self.matrix_size_slider.setValue(4)

    def on_matrix_size_changed(self):
        """
        Se ejecuta cuando el usuario cambia el tamaño de la matriz.
        """
        self.matrix_controller.change_size(self.matrix_size_slider.value())

    # ==================== MÉTODOS AUXILIARES ====================
    def absolute_solver(self):
        '''
        Metodo el cual se encarga de obtener los datos, procesarlos, llamar a las
        funciones de solución y mostrar los resultados.
        '''
        # validaciones
        if not self.carefully_with_max_iterations():
            return

        # Obtener datos de la matriz y parámetros para resolver
        coeficientes, terminos_independientes = self.matrix_controller.separate_A_b()
        tol = float(self.tolerancia_field.text())
        max_iter = int(self.iteraciones_maximas_field.text())

        # Valores de resultado
        detail : ResultDetail = ResultDetail()
        detail.metodo = self.seleccionar_metodo.currentText()
        
        result : ResultHandler = ResultHandler()
        tmp_solucion = []

        # Realizar la operacion
        try:
            print("Using method: ", self.seleccionar_metodo.currentText())

            now = time.time()
            if(self.seleccionar_metodo.currentText() == "Gauss-Seidel"):
                tmp_solucion, detail.total_iterations, detail.converged = gauss_seidel(coeficientes, terminos_independientes, tol=tol, max_iter=max_iter)

            elif(self.seleccionar_metodo.currentText() == "Jacobi"):
                tmp_solucion, detail.total_iterations, detail.converged = jacobi(coeficientes, terminos_independientes, tol=tol, max_iter=max_iter)

            # obtener tiempo de ejecucion
            after = time.time()
            detail.execution_time = after - now

            # obtener solucion
            if(self.result_register is None):
                raise Exception("ResultRegister no está inicializado en SolverPageController.")
            
            print("Solución encontrada: ", tmp_solucion)
            result.set_results(tmp_solucion)
            self.result_register.result_handler = result
            self.result_register.result_detail = detail

            self.result_register.notify()

            # ir a la página de resultados
            self.navigation_controller.set_current_page(RESULT_PAGE_INDEX)

            # Mostrar detalles en un diálogo
            results_dialog = ResultDetailDialogController(detail, self)
            results_dialog.show_results()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            print(e)
            print(e.__traceback__)

    def carefully_with_max_iterations(self):
        '''
        Metodo que se encarga de validar el número máximo de iteraciones
        ingresado por el usuario. Esto es para evitar que la aplicación se congele
        por un número muy alto de iteraciones.

        Returns:
            bool: True si el valor es válido, False en caso contrario.
        '''
        max_iter = int(self.iteraciones_maximas_field.text())

        # valiudar que no sea muy grande
        if max_iter > 10000:
            reply = QMessageBox.question(self, 
                                         'Advertencia',
                                         "El número máximo de iteraciones es muy alto y puede causar que la aplicación se congele. ¿Desea continuar?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                                        )
            if reply == QMessageBox.No:
                return False
            
        # validar que no sea negativo o cero
        if max_iter <= 0:
            QMessageBox.critical(self, "Error", "El número máximo de iteraciones debe ser un entero positivo.")
            return False

        return True
    
    # ==================== MÉTODOS DE LA INTERFAZ ResultInterfaceRegister ====================
    def update_from_result_register(self):
        '''
        Este método se llama para actualizar la interfaz desde el registro de resultados.
        '''
        pass