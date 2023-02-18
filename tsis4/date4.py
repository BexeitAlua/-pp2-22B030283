import datetime as dt

d = dt.datetime(2005, 3 ,20)

d2 = dt.datetime(1969, 12 ,14)

print(dt.timedelta.total_seconds(d - d2))