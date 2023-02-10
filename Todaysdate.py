from calendar import month
from datetime import datetime
now = datetime.now()
month= str(now.month)
dd = str(now.day)
yyyy= str(now. year)
hour = str(now.hour)
min = str(now.minute)
ss = str(now.second)
print (month + "/" + dd + "/" + yyyy + " " + hour + ":" + min + ":" + ss)