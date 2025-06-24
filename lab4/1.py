from datetime import datetime, timedelta, date

# 1
# current_date = date.today()
# five_days_ago = current_date - timedelta(days=5)
# print(current_date)
# print(five_days_ago)

# 2
# today = date.today()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)
# print(today)
# print(yesterday)
# print(tomorrow)

# 3
# now = datetime.now()
# now_without_microseconds = now.replace(microsecond=0)
# print(now)
# print(now_without_microseconds)

# 4
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
diff_seconds = (tomorrow - yesterday).total_seconds()
print(diff_seconds)
