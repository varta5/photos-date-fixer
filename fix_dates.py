from os import listdir
from os.path import isfile

if __name__ == "__main__":
    directories_and_files = listdir()
    filenames = [element for element in directories_and_files if isfile(element)]
    print(f"Current directory contains {len(filenames)} files.")
