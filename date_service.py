from datetime import datetime

class DateService:

    def __init__(self):
        self.datetime_now = datetime.now()
        print(self.datetime_now)

    def get_available_years_descending(self):
        available_years = list(range(1970, self.datetime_now.year  + 1))
        available_years.reverse()
        return available_years

    def get_months_descending(self):
        available_months = list(range(1, 13))
        available_months.reverse()
        return available_months

    def get_days_descending(self):
        available_days = list(range(1, 32))
        available_days.reverse()
        return available_days

    def get_hours_descending(self):
        hours = list(range(24))
        hours.reverse()
        return hours

    def get_minutes_or_seconds_descending(self):
        minutes_or_seconds = list(range(60))
        minutes_or_seconds.reverse()
        return minutes_or_seconds
