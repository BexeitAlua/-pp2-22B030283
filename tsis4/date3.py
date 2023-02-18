import datetime as dt

d = dt.datetime.now()

format= "%d:%m:%Y"
print(d.strftime(format))