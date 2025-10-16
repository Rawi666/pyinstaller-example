#!/bin/bash
# Build single-file executable

pyinstaller --onefile --clean --name myapp app.py
