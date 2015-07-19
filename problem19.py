import datetime
def problem19():
	sundays = 0
	for year in range(1901, 2001):
		for month in range(1, 13):
			if ((datetime.datetime(year, month, 1)).weekday() == 6):
				sundays += 1
	return sundays