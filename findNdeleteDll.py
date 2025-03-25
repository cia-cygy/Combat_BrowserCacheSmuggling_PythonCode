import os

def find_dll_files(directories):
    dll_files = []
    for directory in directories:
        if os.path.exists(directory):
            print(f"Searching in: {directory}")
            for file in os.listdir(directory):
                if file.lower().endswith(".dll"):
                    file_path = os.path.join(directory, file)
                    dll_files.append(file_path)
                    print(f"Found: {file_path}")
        else:
            print(f"Folder not found: {directory}")
    return dll_files

def delete_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

# List of folders to search in
folder_paths = [
    "/Users/deepthi/Library/Caches",
    "/System/Library/CacheDelete",
    "/System/Library/Caches"
]

dll_files = find_dll_files(folder_paths)

if dll_files:
    delete_files(dll_files)
else:
    print("No .dll files found.")