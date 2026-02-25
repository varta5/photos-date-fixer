from os import listdir
from os.path import isfile

from exif_services import ExifServices

PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

if __name__ == "__main__":
    directories_and_files = listdir()
    filenames = [element for element in directories_and_files if isfile(element) and get_file_extension(element.lower()) in PHOTO_FILE_EXTENSIONS]
    print(f"Current directory contains {len(filenames)} files with any of the extensions {PHOTO_FILE_EXTENSIONS}.")

    filenames_to_process = []
    for filename in filenames:
        datetime, datetime_original, datetime_digitized = ExifServices.get_exif_dates(filename)
        if datetime == datetime_original and datetime == datetime_digitized:
            filenames_to_process.append(filename)
        else:
            print(f"{filename} has different datetime among its exif metadata: datetime, datetime_original, datetime_digitized - will not process it")
    print(f"Current directory contains {len(filenames_to_process)} photo files where the datetime exif metadata are consistent.")
