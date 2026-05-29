@echo off
title Lopes' Panel - Instalador
color 04

echo.
echo  [*] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Python nao encontrado!
    echo  Instale em: https://www.python.org/downloads/
    echo  Marque a opcao "Add Python to PATH" durante a instalacao.
    pause
    exit /b 1
)

echo  [OK] Python encontrado.
echo.
echo  [*] Instalando dependencias...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt
echo.
echo  [OK] Instalacao concluida!
echo.
echo  Execute o run.bat para iniciar o Lopes' Panel.
echo.
pause
