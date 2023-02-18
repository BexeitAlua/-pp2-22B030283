import datetime

x = datetime.datetime.today() - datetime.timedelta (5)
format="%Y:%m:%d"
print(x.strftime(format))