import os
import platform
import logging
from datetime import datetime

# -------------------------------------
# 🔐 Setup Logging
# -------------------------------------
# Log file to record deleted files
LOG_FILE = "deleted_files.log"

# Configure logging to write to the log file with timestamp
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------------
# 🌐 Get Browser Cache Folders by OS
# -------------------------------------
def get_browser_cache_dirs():
    home = os.path.expanduser("~")
    system = platform.system()

    paths = []

    if system == "Windows":
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        paths.extend([
            os.path.join(local_app_data, "Google", "Chrome", "User Data", "Default", "Cache"),
            os.path.join(local_app_data, "Mozilla", "Firefox", "Profiles")
        ])
    elif system == "Darwin":  # macOS
        paths.extend([
            os.path.join(home, "Library", "Caches", "Google", "Chrome", "Default", "Cache"),
            os.path.join(home, "Library", "Caches", "Firefox", "Profiles")
        ])
    elif system == "Linux":
        paths.extend([
            os.path.join(home, ".cache", "google-chrome", "Default", "Cache"),
            os.path.join(home, ".cache", "mozilla", "firefox")
        ])
    
    return paths

# -------------------------------------
# 🔍 Find Suspicious Shared Library Files
# -------------------------------------
def find_library_files(directories):
    system = platform.system()
    
    extensions = {
        "Windows": ".dll",
        "Linux": ".so",
        "Darwin": ".dylib"
    }
    lib_ext = extensions.get(system, ".dll")

    found_files = []
    for directory in directories:
        if os.path.exists(directory):
            print(f"🔎 Scanning: {directory}")
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(lib_ext):
                        file_path = os.path.join(root, file)
                        found_files.append(file_path)
                        print(f"⚠️ Found suspicious file: {file_path}")
        else:
            print(f"❌ Directory not found: {directory}")
    return found_files

# -------------------------------------
# 🧹 Delete Files and Log Results
# -------------------------------------
def delete_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"✅ Deleted: {file}")
            logging.info(f"Deleted: {file}")
        except Exception as e:
            print(f"❌ Failed to delete {file}: {e}")
            logging.error(f"Failed to delete {file}: {e}")

# -------------------------------------
# 🏁 Main Execution
# -------------------------------------
def main():
    print("\n🚀 Starting browser cache cleanup...")
    cache_dirs = get_browser_cache_dirs()
    lib_files = find_library_files(cache_dirs)

    if lib_files:
        print(f"\n🧹 Deleting {len(lib_files)} suspicious file(s)...")
        delete_files(lib_files)
        print(f"\n📄 Deletion log saved to: {os.path.abspath(LOG_FILE)}")
    else:
        print("✅ No suspicious shared library files found in browser cache.")

if __name__ == "__main__":
    main()
