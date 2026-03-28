from os import listdir
from os.path import isfile

from exif_services import ExifServices

import datetime as dt
import inquirer

EXIF_DATE_FORMAT = "%Y:%m:%d %H:%M:%S"
PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

def get_desired_datetime_from_user():
    """return datetime of the desired datetime (entered interactively on CLI, based on original_datetime)"""
    questions = [
        inquirer.List("year", message="Select year", choices=[2022, 2023, 2024, 2025, 2026]),
        inquirer.List("month", message="Select month", choices=list(range(1, 13))),
        inquirer.List("day", message="Select day of month", choices=list(range(1, 32))),
        inquirer.List("hour", message="Select hour", choices=list(range(24))),
        inquirer.List("minute", message="Select minute", choices=list(range(60))),
        inquirer.List("second", message="Select second", choices=list(range(60)))
    ]
    answers = inquirer.prompt(questions)
    target_datetime = dt.datetime(
        year=answers["year"],
        month=answers["month"],
        day=answers["day"],
        hour=answers["hour"],
        minute=answers["minute"],
        second=answers["second"]
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
    target_datetime_of_latest_photo = get_desired_datetime_from_user()
    datetime_delta = target_datetime_of_latest_photo - latest_datetime
    print(f"Selected datetime delta: {datetime_delta}")
    print(f"Datetime change of earliest photo: {earliest_datetime} --> {earliest_datetime + datetime_delta}")
    print(f"Datetime change of latest photo: {latest_datetime} --> {target_datetime_of_latest_photo}")
