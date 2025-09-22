import os
import sys

def rename_files(directory, old_ext, new_ext):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    for file in os.listdir(directory):
        if file.endswith(old_ext):
            base = file[:-len(old_ext)]
            new_name = base + new_ext
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            print(f"Renamed: {file} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python DirectoryRename.py <Directory> <OldExt> <NewExt>")
    else:
        rename_files(sys.argv[1], sys.argv[2], sys.argv[3])
