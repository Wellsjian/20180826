import time

def get_day(year,month,day):

   return  (time.time() - time.mktime(time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")))//(3600*24)


print(get_day(1994,4,17))

