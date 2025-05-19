import os

# Function to find all DLL files in the given list of directories
def find_dll_files(directories):
    dll_files = []  # List to store paths of found DLL files
    for directory in directories:
        if os.path.exists(directory):  # Check if the directory exists
            print(f"Searching in: {directory}")
            for file in os.listdir(directory):  # List all files in the directory
                if file.lower().endswith(".dll"):  # Check if the file ends with ".dll"
                    file_path = os.path.join(directory, file)  # Full path of the file
                    dll_files.append(file_path)
                    print(f"Found: {file_path}")
        else:
            print(f"Folder not found: {directory}")
    return dll_files  # Return list of found DLL files

# Function to delete the files in the given list
def delete_files(files):
    for file in files:
        try:
            os.remove(file)  # Attempt to delete the file
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

# List of folders to search in
folder_paths = [
    "/Users/Student/Library/Caches",       # macOS user cache
    "/System/Library/CacheDelete",         # macOS system folder
    "/System/Library/Caches"               # macOS system caches
]

# Find all DLL files in the specified directories
dll_files = find_dll_files(folder_paths)

# Delete found DLL files if any were found
if dll_files:
    delete_files(dll_files)
else:
    print("No .dll files found.")
