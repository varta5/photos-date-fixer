from os import listdir
from os.path import isfile

from exif_services import ExifServices

import datetime as dt

EXIF_DATE_FORMAT = "%Y:%m:%d %H:%M:%S"
PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

def get_desired_datetime_from_user():
    """return datetime of the desired datetime (entered interactively on CLI, based on original_datetime)"""
    target_datetime_properties = {
        "year": 0,
        "month": 0,
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0
    }
    for prop in target_datetime_properties:
        target_datetime_properties[prop] = int(input(f"Please enter desired {prop}:"))
    target_datetime = dt.datetime(
        year=target_datetime_properties["year"],
        month=target_datetime_properties["month"],
        day=target_datetime_properties["day"],
        hour=target_datetime_properties["hour"],
        minute=target_datetime_properties["minute"],
        second=target_datetime_properties["second"]
    )
    return target_datetime

if __name__ == "__main__":
    directories_and_files = listdir()
    filenames = [element for element in directories_and_files if isfile(element) and get_file_extension(element.lower()) in PHOTO_FILE_EXTENSIONS]
    print(f"Current directory contains {len(filenames)} files with any of the extensions {PHOTO_FILE_EXTENSIONS}.")

    filenames_to_process = []
    earliest_datetime = None
    latest_datetime = None
    for filename in filenames:
        datetime_string, datetime_original, datetime_digitized = ExifServices.get_exif_dates(filename)
        if datetime_string != datetime_original or datetime_string != datetime_digitized:
            print(f"{filename} has different datetime among its exif metadata: datetime, datetime_original, datetime_digitized - will not process it")
            continue
        filenames_to_process.append(filename)
        datetime = dt.datetime.strptime(datetime_string, EXIF_DATE_FORMAT)
        if not earliest_datetime or datetime < earliest_datetime:
            earliest_datetime = datetime
        if not latest_datetime or datetime > latest_datetime:
            latest_datetime = datetime
    print(f"Current directory contains {len(filenames_to_process)} photo files where the datetime exif metadata are consistent.")
    print(f"Earliest datetime in the photos: {earliest_datetime}")
    print(f"Latest datetime in the photos: {latest_datetime}")
    target_datetime = get_desired_datetime_from_user()
    datetime_delta = target_datetime - latest_datetime
