### Librerias
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from ui.main_window import Ui_main_window

from controllers.main_page_controller import MainPageController

### Constantes
MAIN_PAGE_INDEX = 0

### Controlador
class MainWindowController(QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Configuracion automatica de la UI
        self.setupUi(self)
        
        # Establecer el widget central (crítico para que se adapte al tamaño)
        self.setCentralWidget(self.centralwidget)

        # Conecta los eventos a tus métodos
        self._connect_signals()
        
        # Inicializa variables o estados si es necesario
        self._initialize_data()

    def _connect_signals(self):
        """
        Conecta las señales de los widgets a los métodos manejadores.
        """
        pass

    def _initialize_data(self):
        """
        Inicializa datos o configuraciones adicionales.
        """
        self._define_pages() # definir las paginas del QStackedWidget

    def _define_pages(self):
        """
        Define y configura las páginas del QStackedWidget.
        """
        # Configuraciones iniciales
        self._delete_default_pages()   # Borrar paginas vacias creadas por Qt Designer
        self.setMinimumSize(800, 600)  # Tamano minimo de la ventana

        # Agregar el panel principal al area de trabajo
        main_page = MainPageController()
        main_page.setVisible(True)
        self.workspace.addWidget(main_page)

        # Mostrar la página principal al iniciar
        self.workspace.setCurrentIndex(MAIN_PAGE_INDEX) 

    def _delete_default_pages(self):
        """
        Elimina las páginas vacías creadas por Qt Designer.
        """
        while self.workspace.count() > 0:
            widget = self.workspace.widget(0)
            self.workspace.removeWidget(widget)

    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================


    # =================== MÉTODOS AUXILIARES ====================