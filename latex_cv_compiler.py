import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os
import sys

def select_project_directory():
    """
    Opens a dialog for the user to select the project directory.
    Validates the presence of 'script.ps1' and 'cv.tex' in the selected directory.
    """
    directory = filedialog.askdirectory()
    if directory:
        script_path = os.path.join(directory, 'script.ps1')
        tex_path = os.path.join(directory, 'cv.tex')
        if not os.path.isfile(script_path):
            messagebox.showerror("File Not Found", f"'script.ps1' not found in {directory}")
            return
        if not os.path.isfile(tex_path):
            messagebox.showerror("File Not Found", f"'cv.tex' not found in {directory}")
            return
        project_path.set(directory)
        log_message(f"Selected Project Directory: {directory}\n")
    else:
        messagebox.showinfo("No Selection", "No directory selected.")

def run_powershell_script():
    """
    Constructs and executes the PowerShell command to run the selected script with elevated privileges.
    Logs the process and handles any exceptions.
    """
    directory = project_path.get()
    if not directory:
        messagebox.showwarning("No Directory", "Please select a project directory first.")
        return

    script_path = os.path.join(directory, 'script.ps1')
    if not os.path.isfile(script_path):
        messagebox.showerror("File Not Found", f"'script.ps1' not found in {directory}")
        return

    # Construct the PowerShell command as per the README
    # This command starts a new PowerShell process with administrator privileges
    # and runs the 'script.ps1' located in the selected directory
    ps_command = (
        f"Start-Process PowerShell -Verb RunAs -ArgumentList "
        f"'-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', "
        f"\"cd '{directory}'; & './script.ps1'\""
    )

    log_message("Executing PowerShell script...\n")
    try:
        # Execute the PowerShell command
        subprocess.run(["powershell", "-Command", ps_command], check=True)
        log_message("PowerShell script executed successfully.\n")
    except subprocess.CalledProcessError as e:
        log_message(f"An error occurred while executing the script:\n{e}\n")
    except Exception as ex:
        log_message(f"Unexpected error: {ex}\n")

def log_message(message):
    """
    Inserts a message into the log text area.
    """
    log_area.config(state='normal')
    log_area.insert(tk.END, message)
    log_area.see(tk.END)
    log_area.config(state='disabled')

def on_closing():
    """
    Handles the window closing event.
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("LaTeX CV Compiler")
root.geometry("600x400")
root.resizable(False, False)

# Define StringVar to hold the project path
project_path = tk.StringVar()

# Create and place the 'Select Project Directory' button
select_button = tk.Button(root, text="Select Project Directory", command=select_project_directory, width=25, height=2)
select_button.pack(pady=10)

# Create and place the label to display the selected directory
path_label = tk.Label(root, textvariable=project_path, wraplength=580, justify="center")
path_label.pack(pady=5)

# Create and place the 'Run Compilation Script' button
run_button = tk.Button(root, text="Run Compilation Script", command=run_powershell_script, width=25, height=2)
run_button.pack(pady=10)

# Create and place the log area using scrolledtext for better usability
log_area = scrolledtext.ScrolledText(root, width=70, height=10, state='disabled', wrap='word')
log_area.pack(pady=10, padx=10)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI event loop
root.mainloop()
