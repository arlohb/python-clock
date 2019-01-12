import time

months=["January","February","March","April","May","June","July","August","September","October""November","December"]

while True:
	timeStruct=time.localtime(time.time())

	month=months[timeStruct.tm_mon-1]
	year=str(timeStruct.tm_year)
	dayNum=str(timeStruct.tm_mday)
	hour=str(timeStruct.tm_hour)
	min=str(timeStruct.tm_min)
	secs=str(timeStruct.tm_sec)
	
	if(len(hour)==1):
		hour="0"+hour
	if(len(min)==1):
		min="0"+min
	if(len(secs)==1):
		secs="0"+secs
	
	print(dayNum+", "+month+", "+year)
	print(hour+":"+min+":"+secs)#
	time.sleep(1)
