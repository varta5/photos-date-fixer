from exif import Image

class ExifServices:

    @staticmethod
    def get_exif_dates(filename):
        """return datetime, datetime_original, datetime_digitized exif properties of a photo file"""
        with open(filename, "rb") as file:
            image = Image(file)
        datetime = image.datetime
        datetime_original = image.datetime_original
        datetime_digitized = image.datetime_digitized
        return datetime, datetime_original, datetime_digitized

    @staticmethod
    def get_image(filename):
        """return exif_image of a photo file"""
        image = None
        with open(filename, "rb") as file:
            image = Image(file)
        return image

    @staticmethod
    def set_dates(image, date_to_set):
        """overwrite datetime exif properties of photo file image object"""
        image.datetime = date_to_set
        image.datetime_original = date_to_set
        image.datetime_digitized = date_to_set
