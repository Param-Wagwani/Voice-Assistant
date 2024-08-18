import os

def open_notepad():
    notepad_path = "C:\\Windows\\System32\\notepad.exe"
    if os.path.exists(notepad_path):
        os.startfile(notepad_path)
        return "Notepad opened."
    else:
        return "Notepad not found."
