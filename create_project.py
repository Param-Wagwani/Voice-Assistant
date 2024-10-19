import os 
import subprocess

def create_vite_project(directory):
    try:
        # Ensure the directory exists
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return

        # Run the command using subprocess in the specified directory
        os.chdir(directory)
        npm_path = r"C:\Program Files\nodejs\npm.cmd"
      
        result = subprocess.run(
            [npm_path, "create", "vite@latest", "my-react-app", "--", "--template", "react"],
            check=True,  # Raise an error if the command fails
            capture_output=True,  # Capture stdout and stderr
            text=True  # Output as string
        )
        # Print the output from the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"Error occurred: {e.stderr}")
