import os

# Function to print contents of a directory
def list_directory_contents(directory):
    try:
        # List all the files and directories
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory}'.")

# Example usage
directory_path = '.'  # Current directory
list_directory_contents('/')
