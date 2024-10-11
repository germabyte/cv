## README.md

# LaTeX CV Compiler

This repository contains a Python-based graphical interface and PowerShell script to automate the process of compiling a LaTeX CV (`cv.tex`) file into a PDF. The system is designed to provide a simple, user-friendly method for compiling LaTeX documents and managing the generated output.

## Features

- **Graphical Interface**: A Python Tkinter GUI allows users to select the project directory and run the compilation process without needing to use the command line.
- **Automated Compilation**: The PowerShell script automatically compiles the LaTeX `cv.tex` file using XeLaTeX and cleans up temporary files, ensuring the output folder only contains the final PDF.
- **Cross-Platform**: While the PowerShell script requires Windows, the Python GUI can run on any system that supports Tkinter, with minor adjustments for Linux/macOS.

## Prerequisites

Before using the system, ensure the following software is installed:

1. **XeLaTeX**: A LaTeX distribution (e.g., MiKTeX or TeX Live) with support for XeLaTeX. You can check if XeLaTeX is installed by running:
   ```bash
   xelatex --version
   ```
2. **Python 3.x**: Required to run the `latex_cv_compiler.py` script. Install it from the [official Python website](https://www.python.org/downloads/).
3. **Tkinter**: Comes bundled with most Python installations. You can verify its installation by trying to import `tkinter` in a Python shell:
   ```python
   import tkinter
   ```

## Usage

### Step 1: Clone the Repository

Clone this repository to your local machine using Git:
```bash
git clone https://github.com/yourusername/latex-cv-compiler.git
cd latex-cv-compiler
```

### Step 2: Prepare Your LaTeX File

Ensure your LaTeX file (`cv.tex`) is in the project directory. You should also ensure the accompanying `script.ps1` is present in the same directory. This script will handle the compilation process.

### Step 3: Run the Python GUI

Run the Python script to open the graphical interface:
```bash
python latex_cv_compiler.py
```

### Step 4: Select the Project Directory

In the GUI:
1. Click the "Select Project Directory" button.
2. Navigate to the folder containing both `cv.tex` and `script.ps1`.
3. The selected directory path will be displayed in the window.

### Step 5: Compile the LaTeX CV

Once the project directory is selected:
1. Click the "Run Compilation Script" button.
2. The PowerShell script will execute the LaTeX compilation process.
3. Check the log output for the progress and any potential errors.

The output will be placed in a folder named `output` within the project directory. Non-PDF files will be automatically removed after compilation.

### Output Files

- The final PDF file will be located in the `output` folder.
- All temporary files (e.g., `.aux`, `.log`) will be deleted.

### Troubleshooting

- **PowerShell Errors**: If the PowerShell script fails to run, ensure PowerShell’s execution policy allows scripts to be run. You can set the execution policy to "Bypass" temporarily with:
  ```bash
  Set-ExecutionPolicy Bypass -Scope Process
  ```

- **File Not Found**: If the Python GUI reports that `cv.tex` or `script.ps1` is missing, ensure that both files are in the same directory and selected correctly in the GUI.

### Customization

- You can modify the `cv.tex` file to include your own CV content, formatting, and structure.
- The `script.ps1` can be adjusted to change the output directory or include additional LaTeX compilation steps if needed.