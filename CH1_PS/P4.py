# print contents of directory  using the os module. [By using ChatGPT]
#this code specify the directory means shows all presents file in "C" drive. {if u wants to see any of folder , u can}
import os  # Import the os module to interact with the operating system

# Define a function to list the contents of a directory
def list_directory_contents(path='.'):
    try:
        # Print the absolute path of the directory being listed
        print(f"Contents of directory: {os.path.abspath(path)}")
        
        # Use os.scandir to iterate through entries in the directory
        with os.scandir(path) as entries:
            for entry in entries:
                # Check if the entry is a file
                if entry.is_file():
                    print(f"File: {entry.name}")
                # Check if the entry is a directory
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
                # Handle other types of entries (e.g., symbolic links, sockets)
                else:
                    print(f"Other: {entry.name}")
    except FileNotFoundError:
        # Handle case where the specified path does not exist
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        # Handle case where the user does not have permission to access the directory
        print(f"Permission denied to access '{path}'.")

# If this script is run directly (not imported as a module)
if __name__ == '__main__':
    # Ask the user to enter a directory path, or press Enter for current directory
    directory_path = input("Enter the path of the directory (leave blank for current directory): ").strip()
    
    # Call the function with the user's input or default to current directory
    list_directory_contents(directory_path if directory_path else '.')
