import os
import subprocess
def open_notepad():
    notepad_path = "C:\\Windows\\System32\\notepad.exe"
    if os.path.exists(notepad_path):
        os.startfile(notepad_path)
        return "Notepad opened."
    else:
        return "Notepad not found."


def open_vscode(path):
    vscode_path = r"C:\Users\calgu\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    
    if path is  None:
        directory_path = r"C:\Users\calgu\OneDrive\Desktop\Voice-Assistant\__pycache__"
    else:
        directory_path = path
    if os.path.exists(vscode_path):
        subprocess.Popen([vscode_path, directory_path])
        return "VS Code opened."

    else:
        return "VS Code not found."