from os import listdir
from os.path import isfile

from exif_services import ExifServices

import datetime as dt

EXIF_DATE_FORMAT = "%Y:%m:%d %H:%M:%S"
PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

if __name__ == "__main__":
    directories_and_files = listdir()
    filenames = [element for element in directories_and_files if isfile(element) and get_file_extension(element.lower()) in PHOTO_FILE_EXTENSIONS]
    print(f"Current directory contains {len(filenames)} files with any of the extensions {PHOTO_FILE_EXTENSIONS}.")

    filenames_to_process = []
    earliest_datetime = None
    latest_datetime = None
    for filename in filenames:
        datetime_string, datetime_original, datetime_digitized = ExifServices.get_exif_dates(filename)
        if datetime_string == datetime_original and datetime_string == datetime_digitized:
            filenames_to_process.append(filename)
            datetime = dt.datetime.strptime(datetime_string, EXIF_DATE_FORMAT)
            if not earliest_datetime or datetime < earliest_datetime:
                earliest_datetime = datetime
            if not latest_datetime or datetime > latest_datetime:
                latest_datetime = datetime
        else:
            print(f"{filename} has different datetime among its exif metadata: datetime, datetime_original, datetime_digitized - will not process it")
    print(f"Current directory contains {len(filenames_to_process)} photo files where the datetime exif metadata are consistent.")
    print(f"Earliest datetime in the photos: {earliest_datetime}")
    print(f"Latest datetime in the photos: {latest_datetime}")
