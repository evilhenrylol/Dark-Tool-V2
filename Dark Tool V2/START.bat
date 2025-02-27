@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

set modules=colorama requests discord rich asyncio threading json base64 subprocess shutil

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install python 3.10.9 or any 3.10.
    pause
    exit /b
)

for %%m in (%modules%) do (
    python -c "import %%m" 2>nul
    if errorlevel 1 (
        echo Installing %%m...
        python -m pip install %%m
    )
)

python Main.py
pause
