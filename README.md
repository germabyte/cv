# README: Compiling LaTeX CV with PowerShell

This README explains how to compile a LaTeX CV using a PowerShell script. It includes instructions for running the script, requirements, and explanations of the various components involved.

## Purpose

The purpose of this project is to automate the compilation of a LaTeX CV document. It uses a PowerShell script to run XeLaTeX twice, ensuring proper generation of cross-references and the table of contents. The script also manages output files, creating a dedicated output directory and cleaning up temporary files after compilation.

## Requirements

Before you begin, ensure you have the following installed on your system:

1. **LaTeX Distribution**: 
   - Install a full TeX Live or MiKTeX distribution, which includes XeLaTeX.
   - Download from: [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/)

2. **PowerShell**: 
   - Windows 10 and later versions come with PowerShell pre-installed.
   - For other systems, download from: [PowerShell GitHub](https://github.com/PowerShell/PowerShell)

3. **Your LaTeX CV file**: 
   - Ensure your CV is saved as `cv.tex` in the project directory.

4. **Any required LaTeX packages**: 
   - The `cv.tex` file may require specific LaTeX packages. Ensure these are installed via your LaTeX distribution's package manager.

## File Structure

Your project directory should look something like this:

```
project-directory/
│
├── cv.tex
├── script.ps1
├── README.md
└── output/  (will be created by the script)
```

## PowerShell Command

To run the compilation script, use the following PowerShell command:

```powershell
Start-Process PowerShell -Verb RunAs -ArgumentList "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "cd 'path\to\your\project'; & '.\script.ps1'"
```

Replace `path\to\your\project` with the actual path to your project directory.

## Generic Examples

1. If your project is in your Documents folder:
   ```powershell
   Start-Process PowerShell -Verb RunAs -ArgumentList "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "cd '$env:USERPROFILE\Documents\cv-project'; & '.\script.ps1'"
   ```

2. If your project is on your Desktop:
   ```powershell
   Start-Process PowerShell -Verb RunAs -ArgumentList "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "cd '$env:USERPROFILE\Desktop\cv-project'; & '.\script.ps1'"
   ```

## Instructions

1. Open a PowerShell terminal.
2. Navigate to your project directory:
   ```powershell
   cd path\to\your\project
   ```
3. Run the PowerShell command provided above.
4. If prompted, allow the script to run with administrator privileges.

## What the Script Does

The `script.ps1` file contains PowerShell commands that:

1. Create an "output" subfolder if it doesn't exist.
2. Run XeLaTeX twice on your `cv.tex` file, outputting results to the "output" folder.
3. Clean up temporary files, keeping only the final PDF in the "output" folder.

## The LaTeX CV File

The `cv.tex` file is your LaTeX source file containing your CV content. It uses various LaTeX packages and commands to structure and style your CV. Ensure this file is properly formatted and contains all necessary content before compilation.

## Troubleshooting

- If you encounter permission issues, ensure you're running PowerShell as an administrator.
- If LaTeX packages are missing, use your LaTeX distribution's package manager to install them.
- Check that all file paths in the script match your actual directory structure.

## Note

Always review scripts before running them with elevated privileges. Modify the paths in the command and script as necessary to match your system's directory structure.
