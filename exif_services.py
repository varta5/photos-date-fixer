from exif import Image

class ExifServices:

    @staticmethod
    def get_exif_dates(filename):
        with open(filename, "rb") as file:
            image = Image(file)
        datetime = image.datetime
        datetime_original = image.datetime_original
        datetime_digitized = image.datetime_digitized
        return datetime, datetime_original, datetime_digitized
