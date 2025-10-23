# Script de utilidad para regenerar archivos UI
# Uso: python build_ui.py

import os
import subprocess
from pathlib import Path

# Directorios
UI_DIR = Path(__file__).parent / 'ui'
CONTROLLERS_DIR = Path(__file__).parent / 'controllers'

def build_ui_files():
    """Convierte todos los archivos .ui a .py"""
    print("🔨 Construyendo archivos UI...")
    
    ui_files = list(UI_DIR.glob('*.ui'))
    
    if not ui_files:
        print("⚠️  No se encontraron archivos .ui en la carpeta 'ui'")
        return
    
    for ui_file in ui_files:
        # Nombre del archivo de salida
        output_file = UI_DIR / f"{ui_file.stem}.py"
        
        print(f"   Convirtiendo {ui_file.name} → {output_file.name}")
        
        # Ejecutar pyuic5
        result = subprocess.run(
            ['pyuic5', '-x', str(ui_file), '-o', str(output_file)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"   ✅ {output_file.name} generado exitosamente")
        else:
            print(f"   ❌ Error al convertir {ui_file.name}")
            print(f"      {result.stderr}")
    
    print("\n✨ Compilación completada")

if __name__ == '__main__':
    build_ui_files()
