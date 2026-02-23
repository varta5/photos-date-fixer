from os import listdir
from os.path import isfile

PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

if __name__ == "__main__":
    directories_and_files = listdir()
    filenames = [element for element in directories_and_files if isfile(element) and get_file_extension(element.lower()) in PHOTO_FILE_EXTENSIONS]
    print(f"Current directory contains {len(filenames)} files with any of the extensions {PHOTO_FILE_EXTENSIONS}.")
