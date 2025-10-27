### Librerias
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from controllers.result_page_controller import ResultPageController
from controllers.solver_page_controller import SolverPageController
from ui.main_window import Ui_main_window

from controllers.main_page_controller import MainPageController
from controllers.navigation_controller import NavigationController

from controllers.metodos import ResultDetail, ResultHandler, ResultRegister

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
        self.navigation_controller = NavigationController()

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
        # Configuraciones iniciales
        self.setMinimumSize(800, 600)  # Tamano minimo de la ventana
        self._config_results()

        self._define_pages() # definir las paginas del QStackedWidget

    def _config_results(self):
        '''
        Configurar la gestión de resultados.
        '''
        
        self.result_handler = ResultHandler()
        self.result_detail = ResultDetail()
        self.result_register = ResultRegister(self.result_handler, self.result_detail)

    def _define_pages(self):
        """
        Define y configura las páginas del QStackedWidget.
        """
        self.navigation_controller.register_workspace(self.workspace)
        self.navigation_controller.register_window_title(self.window_title)

        # Página principal (0)
        main_page = MainPageController(navigation_controller=self.navigation_controller)
        self.navigation_controller.add_page(main_page)

        # Página del solver (1)
        solver_page = SolverPageController(navigation_controller=self.navigation_controller, result_register=self.result_register)
        self.navigation_controller.add_page(solver_page)

        # Página de resultados (2)
        result_page = ResultPageController(navigation_controller=self.navigation_controller, result_register=self.result_register)
        self.navigation_controller.add_page(result_page)
        self.result_register.register_page(result_page)

        # Mostrar la página principal al iniciar
        self.navigation_controller.set_current_page(MAIN_PAGE_INDEX)

    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================
    def on_click_to_back_for_main_page(self):
        self.navigation_controller.set_current_page(MAIN_PAGE_INDEX)

    def on_click_to_open_solver_page(self):
        self.set_current_index(SOLVER_PAGE_INDEX)

    def on_click_to_open_calculator_page(self):
        self.set_current_index(CALCULATOR_PAGE_INDEX)

    # =================== MÉTODOS AUXILIARES ====================