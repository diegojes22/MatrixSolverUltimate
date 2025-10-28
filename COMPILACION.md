# 🚀 Guía de Compilación - MatrixSolverUltimate

Esta guía te explica cómo compilar MatrixSolverUltimate en un ejecutable distribuible (.exe) para Windows.

---

## 📋 Requisitos Previos

1. **Python 3.8 o superior** instalado
2. **Entorno virtual** activado (recomendado)
3. Todas las dependencias instaladas

---

## 🔧 Método 1: Compilación Automática (Recomendado)

### Paso 1: Instalar PyInstaller

```powershell
pip install pyinstaller
```

O instala todas las dependencias con:

```powershell
pip install -r requirements.txt
```

### Paso 2: Ejecutar el script de compilación

```powershell
python build_executable.py
```

El ejecutable se generará en la carpeta `dist/MatrixSolverUltimate.exe`

---

## 🛠️ Método 2: Compilación Manual con PyInstaller

Si prefieres controlar el proceso manualmente:

### Opción A: Ejecutable en un solo archivo (recomendado)

```powershell
pyinstaller --name=MatrixSolverUltimate --windowed --onefile --clean --add-data="ui;ui" --add-data="controllers;controllers" --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtWidgets --hidden-import=numpy main.py
```

### Opción B: Ejecutable con carpeta de dependencias (más rápido)

```powershell
pyinstaller --name=MatrixSolverUltimate --windowed --clean --add-data="ui;ui" --add-data="controllers;controllers" --hidden-import=PyQt5.QtCore --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtWidgets --hidden-import=numpy main.py
```

---

## 📦 Estructura después de compilar

```
MatrixSolverUltimate/
├── dist/
│   └── MatrixSolverUltimate.exe    ← Tu ejecutable final
├── build/                           ← Archivos temporales (puedes borrar)
├── MatrixSolverUltimate.spec        ← Archivo de configuración
└── ... (resto del proyecto)
```

---

## 🎨 Agregar un Icono (Opcional)

1. Consigue o crea un archivo `icon.ico` (icono de Windows)
2. Colócalo en la raíz del proyecto
3. Ejecuta nuevamente `build_executable.py` (detectará el icono automáticamente)

O manualmente:

```powershell
pyinstaller --icon=icon.ico ... (resto de argumentos)
```

---

## ⚙️ Personalización Avanzada

### Editar el archivo .spec

Después de la primera compilación, se genera `MatrixSolverUltimate.spec`. Puedes editarlo para:

- Cambiar el nombre del ejecutable
- Agregar más recursos
- Modificar opciones de compilación

Luego compila usando el .spec:

```powershell
pyinstaller MatrixSolverUltimate.spec
```

### Ejemplo de spec personalizado:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('ui', 'ui'), ('controllers', 'controllers')],
    hiddenimports=['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MatrixSolverUltimate',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'  # Si tienes icono
)
```

---

## 🐛 Solución de Problemas

### Error: "No module named 'PyQt5'"

```powershell
pip install PyQt5
```

### Error: "Failed to execute script"

Prueba con modo carpeta en lugar de `--onefile`:

```powershell
pyinstaller --name=MatrixSolverUltimate --windowed --add-data="ui;ui" --add-data="controllers;controllers" main.py
```

### Error: "RecursionError: maximum recursion depth exceeded"

Agrega al comando:

```powershell
--recursion-limit=5000
```

### El ejecutable es muy grande

Opciones para reducir el tamaño:

1. **Usar UPX** (compresor):
   ```powershell
   pyinstaller ... --upx-dir=C:\ruta\a\upx
   ```

2. **Modo carpeta** en lugar de `--onefile`

3. **Excluir módulos innecesarios**:
   ```powershell
   --exclude-module=matplotlib --exclude-module=pandas
   ```

---

## ✅ Verificación Final

1. Ve a la carpeta `dist/`
2. Ejecuta `MatrixSolverUltimate.exe`
3. Prueba todas las funcionalidades:
   - ✅ Página principal
   - ✅ Calculadora
   - ✅ Solver de matrices
   - ✅ Navegación entre páginas

---

## 📤 Distribución

Una vez compilado, puedes distribuir:

- **Un solo archivo**: `dist/MatrixSolverUltimate.exe` (si usaste `--onefile`)
- **Carpeta completa**: `dist/MatrixSolverUltimate/` (si no usaste `--onefile`)

El usuario final **NO necesita** tener Python instalado.

---

## 🎯 Comandos Rápidos

### Compilación rápida para pruebas:
```powershell
python build_executable.py
```

### Limpiar archivos de compilación:
```powershell
Remove-Item -Recurse -Force build, dist
Remove-Item MatrixSolverUltimate.spec
```

### Compilar y probar:
```powershell
python build_executable.py; .\dist\MatrixSolverUltimate.exe
```

---

## 📝 Notas Importantes

- ⚠️ La primera compilación puede tardar 5-10 minutos
- ⚠️ El ejecutable puede ser detectado como falso positivo por algunos antivirus (normal con PyInstaller)
- ⚠️ El tamaño del ejecutable será ~50-150 MB debido a PyQt5 y numpy
- ✅ Compila en el mismo sistema operativo donde se ejecutará (Windows para .exe)
- ✅ Las compilaciones posteriores son más rápidas (usa `--clean` solo cuando sea necesario)

---

## 🚀 ¡Listo!

Tu aplicación está lista para ser distribuida. Los usuarios pueden ejecutar el `.exe` directamente sin instalar nada adicional.

**¿Problemas?** Revisa la sección de solución de problemas o contacta al desarrollador.
