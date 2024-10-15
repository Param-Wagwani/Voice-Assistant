import os
import subprocess


commands_dict = {
    "open file explorer": ["start", "explorer"],
    "open wi-fi settings": ["start", "ms-settings:network-wifi"],
    "open bluetooth settings": ["start", "ms-settings:bluetooth"],
    "open windows update settings": ["start", "ms-settings:windowsupdate"],
    "open task manager": ["taskmgr"],
    "open notepad": ["notepad"],
    "open calculator": ["calc"],
    "open control panel": ["control"],
    "open command prompt": ["cmd"],
    "open system settings": ["start", "ms-settings:"],
    "open device manager": ["devmgmt.msc"],
    "open disk management": ["diskmgmt.msc"],
    "open registry editor": ["regedit"],
    "open system information": ["msinfo32"],
    "open services manager": ["services.msc"],
    "open network and sharing center": ["start", "ms-settings:network"],
    "open firewall settings": ["start", "ms-settings:windowsdefender"],
    "open windows defender": ["start", "windowsdefender:"],
    "open powershell": ["powershell"],
    "open run dialog": ["start", "Run"],
    "open this pc": ["explorer", "shell:MyComputerFolder"],
    "open programs and features": ["appwiz.cpl"],
    "open event viewer": ["eventvwr"],
    "open remote desktop": ["mstsc"],
    "open magnifier": ["magnify"],
    "open narrator": ["narrator"],
    "open snipping tool": ["snippingtool"],
    "open task scheduler": ["taskschd.msc"],
    "open display settings": ["start", "ms-settings:display"],
    "open sound settings": ["start", "ms-settings:sound"],
    "open battery settings": ["start", "ms-settings:batterysaver-settings"],
    "open personalization settings": ["start", "ms-settings:personalization"],
    "open lock screen settings": ["start", "ms-settings:lockscreen"],
    "open apps and features": ["start", "ms-settings:appsfeatures"],
    "open storage settings": ["start", "ms-settings:storagesense"],
    "open focus assist": ["start", "ms-settings:quietmoments"],
    "open camera": ["start", "microsoft.windows.camera:"],
    "open time and language settings": ["start", "ms-settings:dateandtime"],
    "open ease of access settings": ["start", "ms-settings:easeofaccess"],
    "open privacy settings": ["start", "ms-settings:privacy"],
    "open keyboard settings": ["start", "ms-settings:easeofaccess-keyboard"],
    "open mouse settings": ["start", "ms-settings:mousetouchpad"],
    "open windows search settings": ["start", "ms-settings:cortana-windowssearch"],
    "open network status": ["start", "ms-settings:network-status"],
    "open phone link": ["start", "ms-settings:mobile-devices"],
    "open clipboard settings": ["start", "ms-settings:clipboard"],
    "open windows security": ["start", "windowsdefender:"],
    "open microsoft store": ["start", "ms-windows-store:"],
    "open photos app": ["start", "ms-photos:"],
    "open mail app": ["start", "outlookmail:"],
    "open movies  app": ["start", "mswindowsvideo:"],
    "open groove music": ["start", "mswindowsmusic:"],
    "open people app": ["start", "ms-people:"],
    "open xbox game bar": ["start", "ms-gamingoverlay:"],
    "open alarms and clock": ["start", "ms-clock:"],
    "open paint": ["mspaint"],
    "open snip and sketch": ["start", "ms-screensketch:"],
    "open sticky notes": ["start", "ms-stickynotes:"],
    "open microsoft teams": ["start", "Teams"] ,
"open chrome": ["start", "chrome"],
"open youtube": ["start", "https://www.youtube.com"],
"open netflix": ["start", "https://www.netflix.com"],
"open gmail": ["start", "https://mail.google.com"],
"open outlook": ["start", "outlook"],
"open libreoffice writer": ["start", "soffice", "--writer"],
"open libreoffice calc": ["start", "soffice", "--calc"],
"open libreoffice impress": ["start", "soffice", "--impress"],
"open whatsapp": ["start", "https://web.whatsapp.com"],

}


def execute_command(voice_command):
    # Look up the command in the dictionary
    command_to_run = commands_dict.get(voice_command.lower())
    
    if command_to_run:
        try:
            # Execute the corresponding command using subprocess.run()
            subprocess.run(command_to_run, shell=True)
            print(f"Executed: {voice_command}")
        except Exception as e:
            print(f"Failed to execute {voice_command}: {e}")
    else:
        print(f"Command '{voice_command}' not recognized.")

# Example voice command (replace this with real speech recognition input)
# while(True):
#     voice_input = input("Enter command: ")
#     execute_command(voice_input)





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