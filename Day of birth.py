import calendar
import datetime

from datetime import date, datetime

name = str(input("Enter you name: "))

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))



day_names = [i for i in calendar.day_name]
day_of_week = date(year, month, day).weekday()
day = day_names[day_of_week]

print(f"{name} was born on a day {day}")