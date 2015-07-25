from datetime import datetime
print sum(datetime(year, month, 1).weekday() == 1 for year in range(1901, 2001) for month in range(1,13))