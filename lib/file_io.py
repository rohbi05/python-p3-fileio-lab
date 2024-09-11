import os

def write_file(file_name, file_content):
    """Write content to a file, overwriting any existing content."""
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to a file, creating the file if it does not exist."""
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """Read content from a file and return it. Returns None if file does not exist."""
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as file:
        return file.read()