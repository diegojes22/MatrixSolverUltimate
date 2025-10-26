from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt

from ui.solver_screen import Ui_solver_screen
from controllers.navigation_controller import NavigationController
from controllers.matrix_controller import MatrixController

from controllers.metodos import gauss_seidel, jacobi

class SolverPageController(QWidget, Ui_solver_screen):
    """
    Clase controladora que hereda de QWidget y usa la interfaz generada.
    Aquí va toda tu lógica personalizada.
    """

    def __init__(self, navigation_controller : NavigationController, parent=None):
        super().__init__(parent)
        # Configura la interfaz generada automáticamente
        self.setupUi(self)
        self.navigation_controller : NavigationController = navigation_controller
        self.matrix_controller : MatrixController = MatrixController()
        
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
        coeficientes, terminos_independientes = self.matrix_controller.separate_A_b()
        solucion = []

        try:
            if(self.seleccionar_metodo.currentText() == "Gauss-Seidel"):
                print("Usando Gauss-Seidel")
                solucion = gauss_seidel(coeficientes, terminos_independientes)
                print("Solución:", solucion)
            elif(self.seleccionar_metodo.currentText() == "Jacobi"):
                print("Usando Método Jacobi")
                solucion = jacobi(coeficientes, terminos_independientes)
                print("Solución:", solucion)

        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))