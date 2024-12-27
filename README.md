# LaTeX CV Compiler

This repository provides a Python-based graphical interface and PowerShell script to automate the process of compiling a LaTeX CV (`cv.tex`) file into a PDF. The system offers a straightforward, user-friendly method for compiling LaTeX documents and managing the generated output.

## Features

- **Graphical Interface**: A Python Tkinter GUI enables users to select the project directory and run the compilation process without using the command line.
- **Automated Compilation**: The PowerShell script compiles the LaTeX `cv.tex` file using XeLaTeX and cleans up temporary files, ensuring the output folder only contains the final PDF.
- **Cross-Platform**: While the PowerShell script is tailored for Windows, the Python GUI can run on any system that supports Tkinter, with minor adjustments for Linux/macOS.

## Prerequisites

Before using the system, ensure the following software is installed:

1. **XeLaTeX**: A LaTeX distribution (e.g., MiKTeX or TeX Live) with support for XeLaTeX. Verify installation by running:
   ```bash
   xelatex --version
   ```
2. **Python 3.x**: Required to run the `latex_cv_compiler.py` script. Install it from the [official Python website](https://www.python.org/downloads/).
3. **Tkinter**: Bundled with most Python installations. Confirm its installation by attempting to import it in a Python shell:
   ```python
   import tkinter
   ```

## Usage

### Step 1: Download the Repository

Download this repository as a ZIP file by clicking the **"Code"** button at the top of the repository page on GitHub and selecting **"Download ZIP"**. Extract the contents of the ZIP file to a folder on your computer.

### Step 2: Prepare Your LaTeX File

Ensure your LaTeX file (`cv.tex`) is in the extracted folder. Verify that the `script.ps1` file is also in the same directory. This script will handle the compilation process.

### Step 3: Run the Python GUI

1. Open a terminal or command prompt and navigate to the folder where the repository was extracted.
2. Run the Python script to open the graphical interface:
   ```bash
   python latex_cv_compiler.py
   ```

### Step 4: Select the Project Directory

In the GUI:
1. Click the **"Select Project Directory"** button.
2. Navigate to the folder containing both `cv.tex` and `script.ps1`.
3. The selected directory path will appear in the GUI window.

### Step 5: Compile the LaTeX CV

Once the project directory is selected:
1. Click the **"Run Compilation Script"** button.
2. The PowerShell script will execute the LaTeX compilation process.
3. Monitor the log output in the GUI for progress and any potential errors.

The final PDF will be placed in an `output` folder within the project directory. Non-PDF files will be automatically removed after compilation.

### Output Files

- The compiled PDF will be located in the `output` folder.
- Temporary files (e.g., `.aux`, `.log`) will be deleted automatically.

### Troubleshooting

- **PowerShell Errors**: If the PowerShell script fails to run, ensure PowerShell’s execution policy allows scripts to run. Temporarily set the execution policy to "Bypass" with:
  ```bash
  Set-ExecutionPolicy Bypass -Scope Process
  ```

- **File Not Found**: If the Python GUI reports missing files (`cv.tex` or `script.ps1`), ensure both are present in the selected directory.

### Customization

- Edit the `cv.tex` file to include your CV content, formatting, and structure.
- Adjust the `script.ps1` file to modify the output directory or include additional LaTeX compilation steps if needed.
