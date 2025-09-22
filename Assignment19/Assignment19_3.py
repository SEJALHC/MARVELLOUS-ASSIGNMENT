import os
import sys

def copy_file(src_file, dest_file):
    with open(src_file, 'rb') as fsrc:
        with open(dest_file, 'wb') as fdest:
            while True:
                chunk = fsrc.read(1024)  # 1KB chunks
                if not chunk:
                    break
                fdest.write(chunk)

def copy_all_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print("Source directory does not exist!")
        return

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)
        dest_path = os.path.join(dest_dir, file)
        if os.path.isfile(src_path):
            copy_file(src_path, dest_path)
            print(f"Copied: {file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python DirectoryCopy.py <SourceDir> <DestDir>")
    else:
        copy_all_files(sys.argv[1], sys.argv[2])
