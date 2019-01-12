import time

months=["January","February","March","April","May","June","July","August","September","October""November","December"]

timeStruct=time.localtime(time.time())

month=months[timeStruct.tm_mon-1]
year=str(timeStruct.tm_year)
dayNum=str(timeStruct.tm_mday)

#print(mday,mon,year)
print(dayNum+", "+month+", "+year)
#print(hour,min,secs)
