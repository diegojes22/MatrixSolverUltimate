from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from ui.result_detail_dialog import Ui_Dialog

from controllers.metodos import ResultDetail

#########################################

class ResultDetailDialogController(QDialog, Ui_Dialog):
    '''
    Controlador para el diálogo de detalles del resultado.
    Muestra los detalles del resultado de la solución en un diálogo.
    '''
    def __init__(self, ResultDetail: ResultDetail, parent=None):
        '''
        Constructor del diálogo de detalles del resultado.

        Parámetros:
        - ResultDetail (ResultDetail): Objeto que contiene los detalles del resultado.
        - parent (QWidget, opcional): Widget padre del diálogo.
        '''
        super().__init__(parent)
        self.setupUi(self)

        self.result_detail = ResultDetail
        self._show_data()

    def set_result_detail(self, result_detail: ResultDetail):
        '''
        Establece el detalle del resultado y actualiza la UI.
        Parámetros:
        - result_detail (ResultDetail): Nuevo detalle del resultado.
        '''
        self.result_detail = result_detail
        self._show_data()

    def get_result_detail(self) -> ResultDetail:
        '''
        Obtiene el detalle del resultado actual.
        Retorna:
        - ResultDetail: El detalle del resultado.
        '''
        return self.result_detail
        
    def _show_data(self):
        '''
        Metodo privado para mostrar los datos del resultado en la UI.
        '''
        self.method_name.setText(self.result_detail.get_metodo())
        self.time.setText(f"{self.result_detail.get_execution_time():.3f} seconds")
        self.total_iterations.setText(str(self.result_detail.get_total_iterations()))
        self.converge.setText("Si" if self.result_detail.get_converged() else "No")

    def show_results(self):
        '''
        Este es el método público para mostrar el diálogo con los resultados.
        '''
        self.exec_()

