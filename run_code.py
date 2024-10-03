import os

from search_dir import find_file

def compile_and_run_c_code(filename):
    # Search for the file in the entire directory structure
    file_path = find_file(filename, "D:\\")

    if file_path:
        # Compile the C code
        compile_command = f"gcc {file_path} -o output.exe"
        compile_status = os.system(compile_command)
        
        if compile_status == 0:
            # Run the compiled executable if compilation was successful
            run_command = "output.exe"
            os.system(run_command)
        else:
            print("Compilation failed.")
    else:
        print(f"File {filename} not found.")

def compile_and_run_py_code(filename):
    # Search for the file in the entire directory structure
    file_path = find_file(filename, "D:\\")

    if file_path:
        # Run the Python code
        run_command = f"python {file_path}"
        os.system(run_command)
    else:
        print(f"File {filename} not found.")

# Example usage
compile_and_run_py_code("leap_year.py")