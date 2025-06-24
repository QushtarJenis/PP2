from datetime import date

today = date.today()

month = 11
day = 29
birthday = date(today.year, month, day)
if birthday <= today:
    birthday = date(today.year + 1, month, day)

left_day = (birthday - today).days
print(left_day, "days left")
