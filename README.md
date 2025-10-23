# MatrixSolver - Python Edition

## 📁 Estructura del Proyecto

```
python-edition/
│
├── main.py                      # Punto de entrada principal
├── build_ui.py                  # Script para regenerar archivos UI
│
├── ui/                          # Archivos de interfaz (Qt Designer)
│   ├── __init__.py
│   ├── SelectMenu.ui            # Diseño Qt Designer (editable)
│   └── main_page.py             # Generado automáticamente (NO EDITAR)
│
├── controllers/                 # Lógica de negocio
│   ├── __init__.py
│   └── main_page_controller.py  # Controlador con tu lógica
│
└── env/                         # Entorno virtual de Python
```

---

## 🚀 Flujo de Trabajo

### **1. Activar el entorno virtual**

```powershell
.\env\Scripts\Activate.ps1
```

### **2. Diseñar la interfaz**

- Abre **Qt Designer**
- Edita los archivos `.ui` en la carpeta `ui/`
- Guarda los cambios

### **3. Generar código Python desde UI**

**Opción A - Script automático (recomendado):**
```powershell
python build_ui.py
```

**Opción B - Manualmente:**
```powershell
cd ui
pyuic5 -x SelectMenu.ui -o main_page.py
cd ..
```

### **4. Implementar la lógica**

- Edita los archivos en `controllers/`
- **NUNCA** edites los archivos `.py` generados en `ui/`

### **5. Ejecutar la aplicación**

```powershell
python main.py
```

---

## 📝 Convenciones de Nomenclatura

### **Archivos UI (.ui)**
- `SelectMenu.ui` → Diseño en Qt Designer
- CamelCase para nombres de archivos

### **Archivos generados (.py en ui/)**
- `main_page.py` → Generado automáticamente
- snake_case para nombres de archivos
- **NO EDITAR MANUALMENTE**

### **Controladores (.py en controllers/)**
- `main_page_controller.py` → Tu lógica aquí
- Sufijo `_controller` para identificar fácilmente
- snake_case para nombres de archivos

### **Widgets en Qt Designer**
Usa prefijos descriptivos:
- `btn` → QPushButton → `btnGuardar`
- `lbl` → QLabel → `lblTitulo`
- `txt` → QLineEdit → `txtNombre`
- `cmb` → QComboBox → `cmbPais`

---

## 🏗️ Crear un Nuevo Panel

### **1. Diseña en Qt Designer**
```
ui/NuevoPanelName.ui
```

### **2. Genera el código Python**
```powershell
python build_ui.py
# Genera: ui/nuevo_panel_name.py
```

### **3. Crea el controlador**
```python
# controllers/nuevo_panel_controller.py

from PyQt5.QtWidgets import QWidget
from ui.nuevo_panel_name import Ui_NombreClase

class NuevoPanelController(QWidget, Ui_NombreClase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._connect_signals()
    
    def _connect_signals(self):
        # Conecta eventos aquí
        pass
```

### **4. Úsalo en tu aplicación**
```python
from controllers.nuevo_panel_controller import NuevoPanelController

panel = NuevoPanelController()
panel.show()
```

---

## 🔧 Dependencias

```bash
pip install PyQt5
```

---

## ⚠️ Reglas Importantes

1. **NO edites archivos en `ui/*.py`** - Se regeneran automáticamente
2. **SIEMPRE trabaja en `controllers/`** para tu lógica
3. **Usa `build_ui.py`** después de modificar archivos `.ui`
4. **Activa el entorno virtual** antes de ejecutar

---

## 📚 Recursos

- [Documentación PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Qt Designer Tutorial](https://doc.qt.io/qt-5/qtdesigner-manual.html)
