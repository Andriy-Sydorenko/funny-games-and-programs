#показує календар на поточний місяць поточного року

import calendar
import datetime

date_and_time = datetime.datetime.now()
year = int(date_and_time.strftime("%Y"))
month = int(date_and_time.strftime("%m"))
day = int(date_and_time.strftime("%d"))
print(calendar.month(year, month))