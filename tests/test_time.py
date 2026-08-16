from datetime import datetime
import pytz
from babel.dates import format_datetime

london_tz = pytz.timezone('Europe/London')
now_london = datetime(2053, 5, 23, 7, 0) #datetime.now(london_tz)

# Разные форматы на русском
print(format_datetime(now_london, "d MMMM y", locale='ru'))      # 16 августа 2026
print(format_datetime(now_london, "d MMMM y HH:mm", locale='ru')) # 16 августа 2026 14:30
print(format_datetime(now_london, "EEEE, d MMMM y", locale='ru')) # воскресенье, 16 августа 2026
print(format_datetime(now_london, "d MMM", locale='ru'))          # 16 авг.
print(format_datetime(now_london, "MMMM", locale='ru'))           # августа