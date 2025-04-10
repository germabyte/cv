# 📄 LaTeX CV Compiler

## 1. Introduction and Purpose

### 🎯 Introduction  
This program provides a simple, user-friendly graphical interface for compiling a LaTeX-based CV (`cv.tex`) using PowerShell and XeLaTeX. It automates the compilation process by executing a PowerShell script that generates a clean, formatted PDF from your LaTeX file.

### ❓ Purpose & Problem Statement  
Manually compiling LaTeX documents on Windows can be cumbersome, especially when involving multiple passes and file clean-up. This tool solves that by letting users:

- Select their LaTeX project folder.
- Automatically run a PowerShell script to compile the CV using `xelatex`.
- Clean up unnecessary files afterward — all with the click of a button.

### ✅ Value Proposition  
- **No command-line knowledge needed.**  
- **Clean and organized output:** All non-PDF files are automatically removed.  
- **Error handling and logging included.**  
- **Ideal for Windows users managing their CVs in LaTeX.**

---

## 2. Dependencies (Required Software/Libraries)

The following dependencies are required to run this program effectively:

### 🐍 Python
- **Exact Name:** Python 3.x  
- **Description:** Required to run the GUI-based script (`latex_cv_compiler.py`).  
- **Installation:**  
  Download and install Python from the official website:  
  👉 https://www.python.org/downloads/

### 🧰 tkinter
- **Exact Name:** `tkinter`  
- **Description:** Used to create the graphical interface (GUI).  
- **Installation:**  
  Usually included with standard Python installations. If missing, install using:  
  ```bash
  sudo apt-get install python3-tk  # (Linux)
  ```

### 💻 Windows PowerShell
- **Exact Name:** PowerShell (with administrator privileges)  
- **Description:** Required to execute the `script.ps1` which performs the LaTeX compilation.  
- **Installation:**  
  PowerShell is included by default on most Windows systems.  
  To manually update: https://learn.microsoft.com/en-us/powershell/

### 🧾 XeLaTeX (from TeX distribution)
- **Exact Name:** `xelatex` (included in full TeX distributions)  
- **Description:** Compiles the `cv.tex` file into a PDF.  
- **Installation:**  
  Install a full TeX distribution such as:  
  👉 [MiKTeX (Windows)](https://miktex.org/download)  
  👉 [TeX Live (Cross-platform)](https://www.tug.org/texlive/)

---

## 3. Getting Started (Installation & Execution)

### 🔽 Download the Repository
1. Click the green "**<> Code**" button on the GitHub page.  
2. Select "**Download ZIP**".  
3. Extract the downloaded ZIP file to a convenient location.

### ▶️ Run the Program

#### Step-by-step Instructions:

1. **Open Command Prompt:**
   - Press `Win + R`, type `cmd`, and press Enter.

2. **Navigate to the Extracted Directory:**
   Use the `cd` command to change to the program folder:  
   ```bash
   cd path\to\extracted\folder
   ```

3. **Run the Python Script:**
   ```bash
   python latex_cv_compiler.py
   ```

> 🔒 **Note:** The PowerShell script requires administrator privileges to run correctly.

---

## 4. User Guide (How to Effectively Use the Program)

### 🧭 Program Flow:

1. **Click "Select Project Directory":**  
   - Choose a folder that contains both:
     - `cv.tex` — your LaTeX CV document.
     - `script.ps1` — the provided PowerShell compilation script.

2. **Click "Run Compilation Script":**  
   - This will:
     - Run `xelatex` twice to ensure proper references.
     - Move the output PDF to the `output` folder.
     - Delete all non-PDF files from `output`.

3. **View the Output:**
   - The final `cv.pdf` will be located in the `output` subfolder within the selected directory.

### 🧑‍💻 Expected Inputs:
- A directory containing:
  - `cv.tex` (LaTeX CV file)
  - `script.ps1` (PowerShell script)

### 📤 Program Output:
- A cleaned and compiled PDF version of your CV in:
  ```
  [your-selected-folder]\output\cv.pdf
  ```

### ⚙️ Configurable Settings:
There are no configurable options exposed to the user. The tool is intentionally simple and minimal.

---

## 5. Use Cases and Real-World Examples

### 📌 Use Case 1: Update and Compile a LaTeX CV
**Scenario:** You’ve just updated your CV in `cv.tex`.  
**Action:** Use this tool to quickly compile and generate the updated PDF.  
**Expected Output:** `output/cv.pdf` containing the latest version.

---

### 📌 Use Case 2: Streamline Portfolio Submissions
**Scenario:** You're submitting your CV for a job application and need a quick PDF with no clutter.  
**Action:** Run the compiler to generate a clean PDF, free of log files and other build artifacts.  
**Expected Output:** A polished `cv.pdf` file ready to send.

---

### 📌 Use Case 3: Non-technical User Needs to Compile a LaTeX CV
**Scenario:** A designer or writer who doesn’t use the command line needs to generate a LaTeX CV.  
**Action:** Launch the GUI, select the folder, and click one button.  
**Expected Output:** A correctly compiled CV PDF without needing technical help.

---

## 6. Disclaimer & Important Notices

- This repository and its contents may be updated at any time without notice.  
- Future changes may render portions of this README obsolete.  
- No guarantees are made regarding functionality, compatibility, or correctness.  
- The program and all associated scripts are provided **as-is**.

---

## 7. Tone, Style, and Presentation Guidelines

- Clear and easy-to-follow instructions suitable for non-technical users.  
- No programming knowledge is required to use the software.  
- Clean, structured layout using headings, lists, and code blocks to enhance readability.  
- Objective and impersonal tone throughout the documentation.  
- Visual enhancements (like screenshots) are suggested only if helpful.
