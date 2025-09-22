import os
import sys

def search_files(directory, extension):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    for file in os.listdir(directory):
        if file.endswith(extension):
            print(f"Found: {file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python DirectoryFileSearch.py <Directory> <Extension>")
    else:
        search_files(sys.argv[1], sys.argv[2])
