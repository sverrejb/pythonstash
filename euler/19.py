from datetime import datetime
print sum(datetime(year, month, 13).weekday() == 4 for year in range(1337, 2015) for month in range(1,13))