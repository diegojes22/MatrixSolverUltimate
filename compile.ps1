# Script de instalación y compilación rápida
# MatrixSolverUltimate

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MATRIXSOLVERULTIMATE - COMPILADOR" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
Write-Host "[1/4] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion encontrado" -ForegroundColor Green
} catch {
    Write-Host "✗ Python no está instalado" -ForegroundColor Red
    Write-Host "Por favor instala Python 3.8 o superior desde https://www.python.org" -ForegroundColor Red
    exit 1
}

# Verificar/Activar entorno virtual
Write-Host ""
Write-Host "[2/4] Verificando entorno virtual..." -ForegroundColor Yellow
if (Test-Path "env\Scripts\Activate.ps1") {
    Write-Host "✓ Entorno virtual encontrado, activando..." -ForegroundColor Green
    & ".\env\Scripts\Activate.ps1"
} else {
    Write-Host "⚠ No se encontró entorno virtual" -ForegroundColor Yellow
    Write-Host "Continuando con Python global..." -ForegroundColor Yellow
}

# Instalar dependencias
Write-Host ""
Write-Host "[3/4] Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencias instaladas correctamente" -ForegroundColor Green
} else {
    Write-Host "✗ Error al instalar dependencias" -ForegroundColor Red
    exit 1
}

# Compilar aplicación
Write-Host ""
Write-Host "[4/4] Compilando aplicación..." -ForegroundColor Yellow
python build_executable.py
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  ✓ COMPILACIÓN EXITOSA" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Tu ejecutable está en: .\dist\MatrixSolverUltimate.exe" -ForegroundColor Cyan
    Write-Host ""
    
    # Preguntar si desea ejecutar
    $ejecutar = Read-Host "¿Deseas ejecutar el programa ahora? (S/N)"
    if ($ejecutar -eq "S" -or $ejecutar -eq "s") {
        Start-Process ".\dist\MatrixSolverUltimate.exe"
    }
} else {
    Write-Host ""
    Write-Host "✗ Error durante la compilación" -ForegroundColor Red
    Write-Host "Revisa los errores anteriores" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
