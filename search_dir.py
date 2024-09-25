import os

def find_directory(directory_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if directory_name in dirs:
            return os.path.join(root, directory_name)
    return None

# directory_name = "projects"  
# search_path = "C://"  
# found_path = find_directory(directory_name, search_path)

# if found_path:
#     print(f"Directory '{directory_name}' found at: {found_path}")
# else:
#     print(f"Directory '{directory_name}' not found.")



import re


def find_directory_name(text):
# Regular expression to capture the directory name with spaces between 'in' and 'directory'
    pattern = r'in\s+([A-Za-z0-9_ ]+?)\s+folder'

# Search for the match
    match = re.search(pattern, text)

    # Return the directory name if found, otherwise return None
    if match:
        return match.group(1).strip()  # .strip() to remove leading/trailing spaces
    else:
        return None

# Example usage
# text = "Open VS Code in my projects directory and start working"
# directory_name = find_directory_name(text)

# if directory_name:
#     print(f"Directory name: {directory_name}")
# else:
#     print("No directory name found")

