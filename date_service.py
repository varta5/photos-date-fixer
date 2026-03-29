from datetime import datetime

class DateService:

    def __init__(self):
        self.datetime_now = datetime.now()
        print(self.datetime_now)

    def get_available_years_descending(self):
        """return list of years from current year back to 1970"""
        available_years = list(range(1970, self.datetime_now.year  + 1))
        available_years.reverse()
        return available_years

    def get_months_descending(self):
        """return list of months as tuples: [("Dec", 12) ... ("Jan", 1)]"""
        month_numbers = list(range(1, 13))
        month_numbers.reverse()
        return [(f'{month_number:02d} - {self.datetime_now.replace(month=month_number, day=1).strftime("%b")}', month_number) for month_number in month_numbers]

    def get_days_descending(self):
        """return list of numbers: 31 ... 1"""
        days = list(range(1, 32))
        days.reverse()
        return days

    def get_hours_descending(self):
        """return list of numbers: 23 ... 0"""
        hours = list(range(24))
        hours.reverse()
        return hours

    def get_minutes_or_seconds_descending(self):
        """return list of numbers: 59 ... 0"""
        minutes_or_seconds = list(range(60))
        minutes_or_seconds.reverse()
        return minutes_or_seconds

    def get_modified_datetime_string(self, datetime_string, format, delta):
        """return datetime string in same format as input, increased by delta"""
        datetime_to_be_modified = datetime.strptime(datetime_string, format)
        datetime_to_be_modified += delta
        return datetime_to_be_modified.strftime(format)
