import datetime
td=datetime.datetime.today()
y=datetime.datetime.today()-datetime.timedelta(1)
tmr=datetime.datetime.today()+datetime.timedelta(1)
print('Yesterday: ',y)
print('Today: ',td)
print('Tomorrow: ',tmr)