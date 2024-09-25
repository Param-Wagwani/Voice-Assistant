import os 
import subprocess
import re


def run_git_command(command, project_dir):
    """Run a Git command in the specified project directory."""
    try:
        # Change to the specified directory
        original_dir = os.getcwd()
        os.chdir(project_dir)
        print(['git'] + command.split())
        # Execute the Git command
        result = subprocess.run(['git'] + command.split(), capture_output=True, text=True, check=True)
        
        # Restore the original directory
        os.chdir(original_dir)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def initialize_git_repo(project_dir):
    """Initialize a Git repository in the specified directory."""
    return run_git_command('init', project_dir)


def add_files(project_dir, file_name=None):
    """Add files to the Git staging area in the specified directory."""
    if file_name:
        return run_git_command(f'add {file_name}', project_dir)
    else:
        return run_git_command('add -A', project_dir)
    
def commit_changes(project_dir, message):
    """Commit changes in the specified directory."""
    return run_git_command(f'commit -m "{message}"', project_dir)


def find_commit_message(text):
    # Regular expression to capture the commit message after 'with message'
    pattern = r'with (the)* message\s+(.+)$'
    
    # Search for the match
    match = re.search(pattern, text)
    
    # Return the commit message if found, otherwise return None
    if match:
        return match.group(2).strip()
    else:
        return None

