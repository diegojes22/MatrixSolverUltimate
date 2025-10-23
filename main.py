import sys
from PyQt5.QtWidgets import QApplication

from controllers.main_window_controller import MainWindowController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Ventana principal con navegación entre paneles
    main_window = MainWindowController()
    main_window.show()
    
    sys.exit(app.exec_())