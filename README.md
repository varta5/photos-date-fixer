# photos-date-fixer

Have a bunch of nice photos with incorrect date or time stored in its metadata? No worries! This utility is here to the rescue!

Change the date and time metadata of all the photos in a directory.

## Usage

Run the fix_dates.py with Python interpreter:

```shell
python fix_dates.py
```

The script counts the number of photo files (\*.jpg or \*.jpeg) in the current directory. It finds the earliest and latest date and time stored in the exif metadata of these photos. Then you can select the desired date and time in an interactive manner on the CLI. As a result the script will know what is the time difference between the original and the real dates. At this point you may exit the script (e.g., if the date or time has been set incorrectly). If you proceed, the script will create a directory under the current directory (whose name includes the date and time of running the script - to make sure it is not colliding with other directories). Then it will create a copy in this directory of all the original photos, but with the desired date and time (each one increased or decreased based on the value which you have set previously).
