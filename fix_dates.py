from os import listdir
from os.path import isfile

from date_service import DateService
from exif_services import ExifServices

import datetime as dt
import inquirer

EXIF_DATE_FORMAT = "%Y:%m:%d %H:%M:%S"
PHOTO_FILE_EXTENSIONS = ["jpg", "jpeg"]

def get_file_extension(filename):
    filename_split = filename.lstrip(".").split(".")
    return filename_split.pop() if len(filename_split) >= 2 else ""

def get_desired_datetime_from_user(date_service, original_datetime):
    """return datetime of the desired datetime (entered interactively on CLI, based on original_datetime)"""
    target_year = inquirer.list_input(f"Select desired year: {original_datetime} --> ????-__-__ __:__:__", choices=date_service.get_available_years_descending())
    target_month = inquirer.list_input(f"Select desired month: {original_datetime} --> {target_year}-??-__ __:__:__", choices=date_service.get_months_descending())
    target_day = inquirer.list_input(f"Select desired day: {original_datetime} --> {target_year}-{target_month:02d}-?? __:__:__", choices=date_service.get_days_descending())
    target_hour = inquirer.list_input(f"Select desired hour: {original_datetime} --> {target_year}-{target_month:02d}-{target_day:02d} ??:__:__", choices=date_service.get_hours_descending())
    target_minute = inquirer.list_input(f"Select desired minute: {original_datetime} --> {target_year}-{target_month:02d}-{target_day:02d} {target_hour:02d}:??:__", choices=date_service.get_minutes_or_seconds_descending())
    target_second = inquirer.list_input(f"Select desired second: {original_datetime} --> {target_year}-{target_month:02d}-{target_day:02d} {target_hour:02d}:{target_minute:02d}:??", choices=date_service.get_minutes_or_seconds_descending())
    target_datetime = dt.datetime(
        year=target_year,
        month=target_month,
        day=target_day,
        hour=target_hour,
        minute=target_minute,
        second=target_second
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
    date_service = DateService()
    target_datetime_of_latest_photo = get_desired_datetime_from_user(date_service, latest_datetime)
    datetime_delta = target_datetime_of_latest_photo - latest_datetime
    print(f"Selected datetime delta: {datetime_delta}")
    print(f"Datetime change of earliest photo: {earliest_datetime} --> {earliest_datetime + datetime_delta}")
    print(f"Datetime change of latest photo: {latest_datetime} --> {target_datetime_of_latest_photo}")
