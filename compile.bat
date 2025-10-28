@echo off
REM Script de instalación y compilación rápida para CMD
REM MatrixSolverUltimate

echo ========================================
echo   MATRIXSOLVERULTIMATE - COMPILADOR
echo ========================================
echo.

REM Verificar Python
echo [1/4] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] Python no esta instalado
    echo Por favor instala Python 3.8 o superior desde https://www.python.org
    pause
    exit /b 1
)
echo [OK] Python encontrado
echo.

REM Activar entorno virtual si existe
echo [2/4] Verificando entorno virtual...
if exist "env\Scripts\activate.bat" (
    echo [OK] Activando entorno virtual...
    call env\Scripts\activate.bat
) else (
    echo [!] No se encontro entorno virtual
    echo Continuando con Python global...
)
echo.

REM Instalar dependencias
echo [3/4] Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [X] Error al instalar dependencias
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas
echo.

REM Compilar
echo [4/4] Compilando aplicacion...
python build_executable.py
if %errorlevel% neq 0 (
    echo.
    echo [X] Error durante la compilacion
    pause
    exit /b 1
)

echo.
echo ========================================
echo   [OK] COMPILACION EXITOSA
echo ========================================
echo.
echo Tu ejecutable esta en: .\dist\MatrixSolverUltimate.exe
echo.

pause
