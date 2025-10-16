## PyInstaller Demo Application

A simple demonstration of how to use PyInstaller to create standalone
executables from Python applications on Linux and Windows.

## What is PyInstaller?

PyInstaller is a tool that packages Python applications into standalone
executables that can run on computers without requiring Python to be
installed. It bundles your Python script, the Python interpreter, and all
dependencies into a single executable or directory.

## Project Structure

```
pyinstaller-example/
├── app.py                      # Main Python application
├── requirements.txt            # Python dependencies
├── build_onefile_linux.sh      # Linux: single file build
├── build_onedir_linux.sh       # Linux: directory build
├── build_onefile_windows.bat   # Windows: single file build
├── build_onedir_windows.bat    # Windows: directory build
├── clean.sh                    # Linux: clean build artifacts
├── clean.bat                   # Windows: clean build artifacts
├── README.md                   # This file
```

## Prerequisites

- Python 3.7 or higher

## Installation Steps

### Step 1: Create Virtual Environment

**Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

This installs:
- `colorama`: For colored terminal output
- `python-dateutil`: For advanced date/time operations
- `pyinstaller`: For creating executables

### Step 3: Test the Application

Before building an executable, test that the application works:

```bash
python app.py
```

You should see:
- Colorful welcome message (colorama)
- System information with platform details
- Future date calculation using python-dateutil
- Date parsing demonstration
- Confirmation that all dependencies work

## Building Executables with PyInstaller

PyInstaller offers two main packaging modes:

### Single-File Mode (--onefile)

Creates one executable file containing everything. Slower to start but
easier to distribute.

**Linux:**

```bash
chmod +x build_onefile_linux.sh
./build_onefile_linux.sh
```

Or manually:

```bash
pyinstaller --onefile --clean --name myapp app.py
```

**Windows:**

```cmd
build_onefile_windows.bat
```

Or manually:

```cmd
pyinstaller --onefile --clean --name myapp.exe app.py
```

**Output:** `dist/myapp` (Linux) or `dist/myapp.exe` (Windows)

### Directory Mode (--onedir)

Creates a folder with the executable and dependencies. Faster to start and
easier to debug.

**Linux:**

```bash
chmod +x build_onedir_linux.sh
./build_onedir_linux.sh
```

Or manually:

```bash
pyinstaller --onedir --clean --name myapp app.py
```

**Windows:**

```cmd
build_onedir_windows.bat
```

Or manually:

```cmd
pyinstaller --onedir --clean --name myapp.exe app.py
```

**Output:** `dist/myapp/` directory with executable inside

## PyInstaller Command Explanation

### Basic Command Structure

```bash
pyinstaller [options] your_script.py
```

### Common Options

- `--onefile`: Package everything into a single executable file
- `--onedir`: Package into a directory with the executable and dependencies
  (default)
- `--clean`: Clean PyInstaller cache before building
- `--name NAME`: Name for the executable
- `--noconsole`: Hide console window (useful for GUI apps on Windows)
- `--icon=icon.ico`: Add a custom icon to the executable

### What Happens During Build

1. PyInstaller analyzes your script and finds all imports
2. It collects all dependencies (packages, modules, libraries)
3. It bundles everything with a Python interpreter
4. It creates the executable in the `dist/` directory
5. Build files and specs are saved in `build/` directory

## Running the Executable

### Single-File Executable

**Linux:**

```bash
./dist/myapp
```

**Windows:**

```cmd
dist\myapp.exe
```

### Directory-Based Executable

**Linux:**

```bash
./dist/myapp/myapp
```

**Windows:**

```cmd
dist\myapp\myapp.exe
```

## Distribution

### Single-File

Simply copy the executable file to any compatible system and run it. No
installation required!

### Directory-Based

Copy the entire `dist/myapp/` folder to the target system. Users must run
the executable inside the folder.

## Important Notes

### Cross-Platform Builds

- **Linux executables only run on Linux**
- **Windows executables only run on Windows**
- You must build on the target platform (build on Linux for Linux, on
  Windows for Windows)

### First Run

Single-file executables extract to a temporary directory on first run, so
they may start slower than directory-based executables.

### Antivirus Software

Some antivirus programs may flag PyInstaller executables as suspicious.
This is a false positive. You may need to add an exception.

### File Size

Executables are larger than the original Python script because they include
the Python interpreter and all dependencies (typically 10-50 MB).

### Source Code Protection

PyInstaller compiles Python code to bytecode (.pyc), but this does NOT
provide strong protection:

- **Bytecode can be decompiled** back to readable Python code using tools
  like `uncompyle6` or `decompyle3`
- **Strings are visible** in the executable (API keys, passwords, etc.)
- **Do NOT embed secrets** directly in your code

If you need to protect intellectual property or secrets:

- Use code obfuscation tools (PyArmor, etc.)
- Store secrets in external configuration files or environment variables
- Consider server-side APIs for sensitive operations
- PyInstaller alone is NOT a security solution

## Troubleshooting

### Issue: Module not found error

**Solution:** Install the missing module in your virtual environment and
rebuild.

### Issue: Executable won't start

**Solution:** Try directory mode instead of single-file mode for better
error messages.

### Issue: Slow startup with --onefile

**Solution:** Use --onedir mode for faster startup, or accept the
extraction delay.

### Issue: Hidden imports not detected

**Solution:** Use the `--hidden-import` option:

```bash
pyinstaller --onefile --hidden-import=module_name app.py
```

## Cleaning Up

To remove build artifacts (build/, dist/, and *.spec files), use the
provided clean scripts:

**Linux:**

```bash
chmod +x clean.sh
./clean.sh
```

**Windows:**

```cmd
clean.bat
```

Or manually:

**Linux:**

```bash
rm -rf build dist *.spec
```

**Windows:**

```cmd
rmdir /s /q build dist
del *.spec
```

## Learning Resources

- PyInstaller Documentation: https://pyinstaller.org/
- PyInstaller GitHub: https://github.com/pyinstaller/pyinstaller
- PyInstaller Manual: https://pyinstaller.org/en/stable/
