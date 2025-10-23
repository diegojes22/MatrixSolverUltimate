"""
Controlador para la página principal del MatrixSolver.
Este archivo contiene toda la lógica de negocio separada del archivo UI generado.
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

# Importamos la interfaz generada desde la carpeta ui
from ui.main_page import Ui_main_screen


class MainPageController(QWidget, Ui_main_screen):
    """
    Clase controladora que hereda de QWidget y usa la interfaz generada.
    Aquí va toda tu lógica personalizada.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Configura la interfaz generada automáticamente
        self.setupUi(self)
        
        # Conecta los eventos a tus métodos
        self._connect_signals()
        
        # Inicializa variables o estados si es necesario
        self._initialize_data()
    
    def _connect_signals(self):
        """
        Conecta las señales de los widgets a los métodos manejadores.
        """
        # Hacer los widgets clicables
        self.access_to_solver.mousePressEvent = self.on_solver_clicked
        self.access_for_calculator.mousePressEvent = self.on_calculator_clicked
        self.access_to_chat.mousePressEvent = self.on_chat_clicked
        self.access_to_help.mousePressEvent = self.on_help_clicked

        # Tooltip para ayuda
        self.access_to_help.setToolTip("Mirar la ayuda")
    
    def _initialize_data(self):
        """
        Inicializa datos o configuraciones adicionales.
        """
        # Ejemplo: configurar cursores para indicar que son clicables
        self.access_to_solver.setCursor(Qt.PointingHandCursor)
        self.access_for_calculator.setCursor(Qt.PointingHandCursor)
        self.access_to_chat.setCursor(Qt.PointingHandCursor)
        self.access_to_help.setCursor(Qt.PointingHandCursor)
    
    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================
    
    def on_solver_clicked(self, event):
        """
        Se ejecuta cuando el usuario hace clic en "Nuevo problema".
        """
        print("Abriendo solver de matrices...")
        # Aquí puedes:
        # - Abrir otra ventana
        # - Cambiar de panel
        # - Emitir una señal personalizada
        # Ejemplo:
        # self.open_solver_window()
    
    def on_calculator_clicked(self, event):
        """
        Se ejecuta cuando el usuario hace clic en "Calculadora".
        """
        print("Abriendo calculadora...")
        # Lógica para abrir la calculadora
    
    def on_chat_clicked(self, event):
        """
        Se ejecuta cuando el usuario hace clic en "Chat Bot".
        """
        print("Abriendo chat bot...")
        # Lógica para abrir el chat bot
    
    def on_help_clicked(self, event):
        """
        Se ejecuta cuando el usuario hace clic en el botón de ayuda.
        """
        print("Mostrando ayuda...")
        # Lógica para mostrar ayuda
    
    # ==================== MÉTODOS DE LÓGICA DE NEGOCIO ====================
    
    def open_solver_window(self):
        """
        Abre la ventana del solver de matrices.
        """
        # Implementa aquí la lógica para abrir otra ventana
        pass
    
    def open_calculator_window(self):
        """
        Abre la ventana de la calculadora.
        """
        pass
    
    def open_chat_window(self):
        """
        Abre la ventana del chat bot.
        """
        pass
    
    def show_help_dialog(self):
        """
        Muestra un diálogo de ayuda.
        """
        pass


# Código para ejecutar esta ventana de forma independiente (opcional)
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = MainPageController()
    window.show()
    sys.exit(app.exec_())
