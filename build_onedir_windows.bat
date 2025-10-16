@echo off
REM Build directory-based executable

pyinstaller --onedir --clean --name myapp app.py
