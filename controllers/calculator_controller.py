from ui.calculator_page import Ui_Form
from PyQt5.QtWidgets import QWidget, QMessageBox

class CalculatorController(QWidget, Ui_Form):
    """
    Controlador para la página de la calculadora del MatrixSolver.
    Este archivo contiene toda la lógica de negocio separada del archivo UI generado.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Configura la interfaz generada automáticamente
        self.setupUi(self)
        
        # Variables de estado
        self.current_value = ""
        self.previous_value = ""
        self.operation = None
        self.new_operation = True
        
        # Inicializar
        self._initialize_data()
        self._connect_signals()
    
    def _initialize_data(self):
        """
        Inicializa datos o configuraciones adicionales.
        """
        self.calculator_screen.setDigitCount(15)
        self.calculator_screen.display(0)
        
    def _connect_signals(self):
        """
        Conecta las señales de los botones a sus respectivos métodos.
        """
        # Conectar botones numéricos
        self.number_0_button.clicked.connect(lambda: self._on_number_clicked("0"))
        self.number_1_button.clicked.connect(lambda: self._on_number_clicked("1"))
        self.number_2_button.clicked.connect(lambda: self._on_number_clicked("2"))
        self.number_3_button.clicked.connect(lambda: self._on_number_clicked("3"))
        self.number_4_button.clicked.connect(lambda: self._on_number_clicked("4"))
        self.number_5_button.clicked.connect(lambda: self._on_number_clicked("5"))
        self.number_6_button.clicked.connect(lambda: self._on_number_clicked("6"))
        self.number_7_button.clicked.connect(lambda: self._on_number_clicked("7"))
        self.number_8_button.clicked.connect(lambda: self._on_number_clicked("8"))
        self.number_9_button.clicked.connect(lambda: self._on_number_clicked("9"))
        
        # Conectar botón de punto decimal
        self.point_button.clicked.connect(self._on_point_clicked)
        
        # Conectar botones de operaciones
        self.sum_button.clicked.connect(lambda: self._on_operation_clicked("+"))
        self.rest_button.clicked.connect(lambda: self._on_operation_clicked("-"))
        self.multiplication_button.clicked.connect(lambda: self._on_operation_clicked("*"))
        self.division_button.clicked.connect(lambda: self._on_operation_clicked("/"))
        self.exp_button.clicked.connect(lambda: self._on_operation_clicked("^"))
        self.porcent_button.clicked.connect(lambda: self._on_operation_clicked("%"))
        
        # Conectar botones especiales
        self.equal_button.clicked.connect(self._on_equal_clicked)
        self.clear_screen_button.clicked.connect(self._on_clear_clicked)
        self.backspace_button.clicked.connect(self._on_backspace_clicked)
    
    def _on_number_clicked(self, number):
        """
        Maneja el clic en un botón numérico.
        """
        if self.new_operation:
            self.current_value = number
            self.new_operation = False
        else:
            # Limitar la longitud para evitar overflow en el display
            if len(self.current_value) < 15:
                self.current_value += number
        
        self._update_display()
    
    def _on_point_clicked(self):
        """
        Maneja el clic en el botón de punto decimal.
        """
        if self.new_operation:
            self.current_value = "0."
            self.new_operation = False
        elif "." not in self.current_value:
            if not self.current_value:
                self.current_value = "0."
            else:
                self.current_value += "."
        
        self._update_display()
    
    def _on_operation_clicked(self, op):
        """
        Maneja el clic en un botón de operación.
        """
        if not self.current_value and not self.previous_value:
            return
        
        # Si ya hay una operación pendiente, calcular primero
        if self.operation and not self.new_operation:
            self._calculate()
        
        # Guardar el valor actual como valor previo
        if self.current_value:
            self.previous_value = self.current_value
        
        self.operation = op
        self.new_operation = True
    
    def _on_equal_clicked(self):
        """
        Maneja el clic en el botón de igual.
        """
        if self.operation and self.current_value:
            self._calculate()
    
    def _on_clear_clicked(self):
        """
        Limpia la pantalla y reinicia la calculadora.
        """
        self.current_value = ""
        self.previous_value = ""
        self.operation = None
        self.new_operation = True
        self.calculator_screen.display(0)
    
    def _on_backspace_clicked(self):
        """
        Elimina el último dígito ingresado.
        """
        if not self.new_operation and self.current_value:
            self.current_value = self.current_value[:-1]
            self._update_display()
    
    def _calculate(self):
        """
        Realiza el cálculo basado en la operación actual.
        """
        try:
            num1 = float(self.previous_value)
            num2 = float(self.current_value)
            result = 0
            
            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y if y != 0 else self._show_error("División por cero"),
                "^": lambda x, y: x ** y,
                "%": lambda x, y: x % y if y != 0 else self._show_error("División por cero")
            }
            
            if self.operation in operations:
                result = operations[self.operation](num1, num2)
                
                if result is None:  # Error detectado
                    return
                
                # Formatear el resultado para evitar números muy largos
                if abs(result) < 1e-10:
                    result = 0
                elif abs(result) > 1e10 or abs(result) < 1e-10:
                    # Notación científica para números muy grandes o pequeños
                    self.current_value = f"{result:.6e}"
                else:
                    # Limitar decimales para números normales
                    self.current_value = str(round(result, 10))
                    # Eliminar ceros innecesarios
                    if "." in self.current_value:
                        self.current_value = self.current_value.rstrip("0").rstrip(".")
                
                self.previous_value = ""
                self.operation = None
                self.new_operation = True
                self._update_display()
                
        except ValueError:
            self._show_error("Error de formato")
        except Exception as e:
            self._show_error(f"Error: {str(e)}")
    
    def _update_display(self):
        """
        Actualiza el display de la calculadora con el valor actual.
        """
        if self.current_value:
            try:
                display_value = float(self.current_value)
                self.calculator_screen.display(display_value)
            except ValueError:
                # Si no se puede convertir, mostrar como texto (ej: "0.")
                self.calculator_screen.display(self.current_value)
        else:
            self.calculator_screen.display(0)
    
    def _show_error(self, message):
        """
        Muestra un mensaje de error.
        """
        QMessageBox.warning(self, "Error", message)
        self._on_clear_clicked()
        return None