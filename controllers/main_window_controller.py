### Librerias
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from ui.main_window import Ui_main_window

from controllers.main_page_controller import MainPageController

### Constantes
MAIN_PAGE_INDEX = 0
SOLVER_PAGE_INDEX = 1
CALCULATOR_PAGE_INDEX = 2
AI_CHAT_PAGE_INDEX = 3
HELP_PAGE_INDEX = 4

### Controlador
class MainWindowController(QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        ''' Constructor '''
        super().__init__(parent)
        self.current_index = MAIN_PAGE_INDEX

        # Configuracion automatica de la UI
        self.setupUi(self)
        
        # Establecer el widget central (crítico para que se adapte al tamaño)
        self.setCentralWidget(self.centralwidget)

        # Conecta los eventos a tus métodos
        self._connect_signals()
        
        # Inicializa variables o estados si es necesario
        self._initialize_data()

    ### Metodos privados
    def _connect_signals(self):
        """
        Conecta las señales de los widgets a los métodos manejadores.
        """
        self.btn_for_back_main_page.clicked.connect(self.on_click_to_back_for_main_page)

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

    def _set_page_name(self):
        page_titles = {
            MAIN_PAGE_INDEX: "Página Principal",
            SOLVER_PAGE_INDEX: "Página de Resolución",
            CALCULATOR_PAGE_INDEX: "Página de Cálculo",
            AI_CHAT_PAGE_INDEX: "Página de Chat AI",
            HELP_PAGE_INDEX: "Página de Ayuda"
        }
        
        title = page_titles.get(self.current_index, "Página Desconocida")
        self.window_title.setText(title)

    ### Getters y Setters
    def set_current_index(self, index):
        '''
        Establecer la página actual del QStackedWidget por su índice.
        '''
        if(index > self.workspace.count()):
            print("La pagina marcada por el indice no existe en el espacio de trabajo!")
            return
            
        self.current_index = index
        self.workspace.setCurrentIndex(index)
        self._set_page_name()

    def get_current_index(self):
        '''
        Obtener el índice de la página actual del QStackedWidget.
        '''
        return self.current_index
    
    ### Otros
    def go_to_main_page(self):
        '''
        Navegar a la página principal.
        '''
        self.set_current_index(MAIN_PAGE_INDEX)

    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================
    def on_click_to_back_for_main_page(self):
        self.go_to_main_page()

    def on_click_to_open_solver_page(self):
        self.set_current_index(SOLVER_PAGE_INDEX)

    def on_click_to_open_calculator_page(self):
        self.set_current_index(CALCULATOR_PAGE_INDEX)

    # =================== MÉTODOS AUXILIARES ====================