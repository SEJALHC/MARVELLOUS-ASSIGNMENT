import os
import sys

def copy_file(src_file, dest_file):
    
    with open(src_file, 'rb') as fsrc:
        with open(dest_file, 'wb') as fdest:
            while True:
                chunk = fsrc.read(1024)  
                if not chunk:
                    break
                fdest.write(chunk)

def copy_with_ext(src, dest, ext):
    if not os.path.exists(src):
        print("Source directory does not exist!")
        return

    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(src):
        if file.endswith(ext):
            src_path = os.path.join(src, file)
            dest_path = os.path.join(dest, file)
            if os.path.isfile(src_path):
                copy_file(src_path, dest_path)
                print(f"Copied: {file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python DirectoryCopyExt.py <SourceDir> <DestDir> <Extension>")
    else:
        copy_with_ext(sys.argv[1], sys.argv[2], sys.argv[3])
