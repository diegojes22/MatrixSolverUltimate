from PyQt5.QtWidgets import QStackedWidget, QLabel

### Constantes
MAIN_PAGE_INDEX = 0
SOLVER_PAGE_INDEX = 1
CALCULATOR_PAGE_INDEX = 2
AI_CHAT_PAGE_INDEX = 3
HELP_PAGE_INDEX = 4
PREMIUM_AD_PAGE_INDEX = 5

page_titles = {
    MAIN_PAGE_INDEX: "Página Principal",
    SOLVER_PAGE_INDEX: "Resolver Sistema de Ecuaciones",
    CALCULATOR_PAGE_INDEX: "Calculadora",
    AI_CHAT_PAGE_INDEX: "Chat AI",
    HELP_PAGE_INDEX: "Ayuda",
    PREMIUM_AD_PAGE_INDEX: "Planes de Suscripción"
}

class NavigationController:
    def __init__(self):
        self.current_index = MAIN_PAGE_INDEX

    def get_current_index(self):
        '''
        Obtiene el índice de la página actual del QStackedWidget.
        '''
        return self.current_index
    
    def set_default_page(self):
        '''
        Establece la página predeterminada (página principal).
        '''
        self.set_current_page(MAIN_PAGE_INDEX)

    def register_workspace(self, workspace):
        '''
        Registra el QStackedWidget que actúa como espacio de trabajo.
        '''
        self.workspace : QStackedWidget = workspace
        self.clear_page()

    def register_window_title(self, window_title_label):
        '''
        Registra la etiqueta que muestra el título de la ventana.
        '''
        self.window_title_label : QLabel = window_title_label

    def add_page(self, page_widget):
        '''
        Agrega una nueva página al QStackedWidget.
        '''
        self.workspace.addWidget(page_widget)

    def set_current_page(self, index):
        '''
        Establece la página actual del QStackedWidget por su índice.
        '''
        if index >= self.workspace.count():
            print("La página marcada por el índice no existe en el espacio de trabajo!")
            return
            
        self.current_index = index
        self.workspace.setCurrentIndex(index)
        self.window_title_label.setText(page_titles.get(index, "Página Desconocida"))

    def clear_page(self):
        '''
        Elimina todas las páginas del QStackedWidget.
        '''
        while self.workspace.count() > 0:
            widget = self.workspace.widget(0)
            self.workspace.removeWidget(widget)