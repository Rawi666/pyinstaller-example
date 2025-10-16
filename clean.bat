@echo off
REM Clean build artifacts

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec
echo Clean complete
