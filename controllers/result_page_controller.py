from ui.result_dialog import Ui_Form
from PyQt5.QtWidgets import QWidget

from controllers.navigation_controller import SOLVER_PAGE_INDEX

from controllers.metodos import ResultDetail, ResultInterfaceRegister, ResultRegister

class ResultPageController(QWidget, Ui_Form, ResultInterfaceRegister):
    def __init__(self, navigation_controller, result_register : ResultRegister = None):
        super().__init__()
        self.navigation_controller = navigation_controller
        self.result_register : ResultRegister = result_register
        self.setup_ui()

        self._connect_signals()

    def _connect_signals(self):
        self.regresar_btn.clicked.connect(self.on_regresar_clicked)

    def setup_ui(self):
        # Configurar la interfaz de usuario para la página de resultados
        self.setupUi(self)

    # ==================== MÉTODOS MANEJADORES DE EVENTOS ====================
    def on_regresar_clicked(self):
        self.navigation_controller.set_current_page(SOLVER_PAGE_INDEX)

    # ==================== MÉTODOS DE INTERFAZ DE RESULTADOS ====================
    def update_from_result_register(self):
        self.lista_soluciones.clear()

        if self.result_register.get_result_handler() is None or self.result_register.get_result_handler().size() == 0:
            return

        solutions = self.result_register.get_result_handler().get_results()

        var_no = 1
        
        for sol in solutions:
            self.lista_soluciones.addItem(f"X{var_no} = {sol}")
            var_no += 1