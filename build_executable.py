"""
Script para compilar MatrixSolverUltimate en un ejecutable
Ejecuta este archivo para crear el ejecutable de la aplicación
"""
import PyInstaller.__main__
import os
import sys

def build_executable():
    """
    Compila la aplicación en un ejecutable usando PyInstaller
    """
    # Ruta base del proyecto
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Argumentos para PyInstaller
    args = [
        'main.py',                              # Archivo principal
        '--name=MatrixSolverUltimate',          # Nombre del ejecutable
        '--windowed',                           # Sin consola (GUI)
        '--onefile',                            # Un solo archivo ejecutable
        '--clean',                              # Limpiar cache antes de compilar
        
        # Incluir carpetas necesarias
        f'--add-data=ui{os.pathsep}ui',
        f'--add-data=controllers{os.pathsep}controllers',
        
        # Hooks ocultos para PyQt5
        '--hidden-import=PyQt5.QtCore',
        '--hidden-import=PyQt5.QtGui',
        '--hidden-import=PyQt5.QtWidgets',
        '--hidden-import=numpy',
        
        # Directorio de salida
        '--distpath=dist',
        '--workpath=build',
        '--specpath=.',
        
        # Optimizaciones
        '--optimize=2',
    ]
    
    # Si existe un icono, agregarlo
    icon_path = os.path.join(base_path, 'icon.ico')
    if os.path.exists(icon_path):
        args.append(f'--icon={icon_path}')
    
    print("=" * 70)
    print("COMPILANDO MATRIXSOLVERULTIMATE")
    print("=" * 70)
    print("\nEsto puede tardar varios minutos...\n")
    
    # Ejecutar PyInstaller
    PyInstaller.__main__.run(args)
    
    print("\n" + "=" * 70)
    print("COMPILACIÓN COMPLETADA")
    print("=" * 70)
    print(f"\nEl ejecutable se encuentra en: {os.path.join(base_path, 'dist', 'MatrixSolverUltimate.exe')}")
    print("\n¡Listo para distribuir!")

if __name__ == "__main__":
    try:
        build_executable()
    except Exception as e:
        print(f"\nError durante la compilación: {e}")
        sys.exit(1)
