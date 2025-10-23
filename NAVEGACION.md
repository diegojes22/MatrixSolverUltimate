# 🔄 Sistema de Navegación entre Paneles

## Concepto

En lugar de abrir ventanas nuevas, usamos **QStackedWidget** que funciona como una pila de cartas: todas las pantallas están cargadas, pero solo una es visible a la vez.

---

## 🏗️ Arquitectura

```
MainWindow (QMainWindow)
    └── QStackedWidget (centralWidget)
            ├── [0] MainPageController (Menú)
            ├── [1] SolverController (Solver)
            ├── [2] CalculatorController (Calculadora)
            └── [3] ChatController (Chat Bot)
```

---

## 📝 Cómo Agregar un Nuevo Panel

### **Paso 1: Diseña la interfaz en Qt Designer**

```
ui/SolverScreen.ui
```

### **Paso 2: Genera el código Python**

```powershell
# Desde la carpeta raíz
python build_ui.py

# O manualmente
cd ui
pyuic5 -x SolverScreen.ui -o solver_screen.py
```

### **Paso 3: Crea el controlador**

```python
# controllers/solver_controller.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui.solver_screen import Ui_SolverScreen

class SolverController(QWidget, Ui_SolverScreen):
    # Señal para comunicarse con la ventana principal
    go_back_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._connect_signals()
    
    def _connect_signals(self):
        # Ejemplo: botón de volver
        if hasattr(self, 'btn_back'):
            self.btn_back.clicked.connect(self.go_back)
    
    def go_back(self):
        """Emite señal para volver al menú."""
        self.go_back_signal.emit()
```

### **Paso 4: Registra el panel en MainWindow**

Edita `controllers/main_window.py`:

```python
from controllers.solver_controller import SolverController

class MainWindow(QMainWindow):
    # Actualiza los índices
    PAGE_MENU = 0
    PAGE_SOLVER = 1
    PAGE_CALCULATOR = 2
    PAGE_CHAT = 3
    
    def _init_panels(self):
        # ... código del menú ...
        
        # Panel 1: Solver (reemplaza el placeholder)
        self.solver_page = SolverController()
        self.solver_page.go_back_signal.connect(self.show_menu)
        self.stacked_widget.addWidget(self.solver_page)
        
        # ... resto de paneles ...
```

---

## 🎯 Navegación entre Paneles

### **Desde MainWindow (principal)**

```python
# En main_window.py
def show_solver(self):
    self.stacked_widget.setCurrentIndex(self.PAGE_SOLVER)
```

### **Desde un Panel (usando señales)**

```python
# En solver_controller.py
class SolverController(QWidget, Ui_SolverScreen):
    go_back_signal = pyqtSignal()
    
    def on_back_clicked(self):
        self.go_back_signal.emit()  # Emite señal

# En main_window.py
def _init_panels(self):
    self.solver_page = SolverController()
    self.solver_page.go_back_signal.connect(self.show_menu)  # Conecta
```

### **Navegación directa con referencia al padre**

```python
# Alternativa: pasar referencia de MainWindow
class SolverController(QWidget, Ui_SolverScreen):
    def __init__(self, main_window=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
    
    def on_back_clicked(self):
        if self.main_window:
            self.main_window.show_menu()
```

---

## 📊 Pasar Datos entre Paneles

### **Método 1: A través de MainWindow**

```python
# En main_window.py
class MainWindow(QMainWindow):
    def show_solver(self, matrix_size=3):
        self.solver_page.set_matrix_size(matrix_size)
        self.stacked_widget.setCurrentIndex(self.PAGE_SOLVER)

# En solver_controller.py
class SolverController(QWidget, Ui_SolverScreen):
    def set_matrix_size(self, size):
        self.current_size = size
        self.update_matrix_display()
```

### **Método 2: Usando señales con parámetros**

```python
# En solver_controller.py
class SolverController(QWidget, Ui_SolverScreen):
    result_ready = pyqtSignal(dict)  # Envía resultados
    
    def calculate(self):
        result = {"solution": [...], "steps": [...]}
        self.result_ready.emit(result)

# En main_window.py
def _init_panels(self):
    self.solver_page = SolverController()
    self.solver_page.result_ready.connect(self.on_solver_result)

def on_solver_result(self, result):
    print(f"Resultado: {result}")
    # Guarda o pasa a otro panel
```

---

## 🎨 Ejemplo: Panel del Solver (según tu diseño de Figma)

```python
# controllers/solver_controller.py

from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import pyqtSignal
from ui.solver_screen import Ui_SolverScreen

class SolverController(QWidget, Ui_SolverScreen):
    go_back_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.matrix_size = 3
        self.matrix_inputs = []
        self._connect_signals()
    
    def _connect_signals(self):
        # Botón volver
        self.btn_back.clicked.connect(self.go_back)
        
        # Botón resolver
        self.btn_resolver.clicked.connect(self.solve_system)
        
        # Botón limpiar
        self.btn_limpiar.clicked.connect(self.clear_matrix)
        
        # Slider de tamaño
        self.slider_size.valueChanged.connect(self.on_size_changed)
        
        # Dropdown de método
        self.cmb_metodo.currentTextChanged.connect(self.on_method_changed)
    
    def on_size_changed(self, size):
        """Actualiza el tamaño de la matriz."""
        self.matrix_size = size
        self.lbl_size.setText(f"{size}×{size}")
        self.generate_matrix_inputs()
    
    def generate_matrix_inputs(self):
        """Genera dinámicamente los inputs de la matriz."""
        # Limpia inputs anteriores
        for input_widget in self.matrix_inputs:
            input_widget.deleteLater()
        self.matrix_inputs.clear()
        
        # Crea nuevos inputs según el tamaño
        for row in range(self.matrix_size):
            for col in range(self.matrix_size + 1):  # +1 para columna de igualdad
                input_field = QLineEdit()
                input_field.setPlaceholderText("0")
                # Agrega al layout correspondiente
                self.grid_matrix.addWidget(input_field, row, col)
                self.matrix_inputs.append(input_field)
    
    def solve_system(self):
        """Resuelve el sistema de ecuaciones."""
        print(f"Resolviendo con método: {self.cmb_metodo.currentText()}")
        # Aquí va tu lógica de resolución
    
    def clear_matrix(self):
        """Limpia todos los campos."""
        for input_widget in self.matrix_inputs:
            input_widget.clear()
    
    def on_method_changed(self, method):
        """Cambia el método de resolución."""
        print(f"Método seleccionado: {method}")
    
    def go_back(self):
        """Vuelve al menú principal."""
        self.go_back_signal.emit()
```

---

## ⚡ Ventajas de este Enfoque

✅ **Sin ventanas múltiples:** Todo en una sola ventana  
✅ **Transiciones suaves:** Cambios instantáneos  
✅ **Gestión de estado:** Cada panel mantiene su estado  
✅ **Comunicación fácil:** Señales entre paneles  
✅ **Escalable:** Agregar paneles es simple  
✅ **Navegación controlada:** MainWindow orquesta todo

---

## 🚀 Próximos Pasos

1. **Diseña el SolverScreen en Qt Designer** según tu mockup de Figma
2. **Genera el código Python** con `python build_ui.py`
3. **Crea SolverController** con la lógica
4. **Registra en MainWindow** y conecta las señales
5. **Prueba la navegación** Menu → Solver → Menu

---

## 💡 Tips

- Usa **señales personalizadas** para comunicación entre paneles
- Mantén **MainWindow ligero**, solo navegación
- La **lógica de negocio** va en cada controlador
- Considera usar **QPropertyAnimation** para transiciones suaves
