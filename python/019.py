import calendar

sundays = 0
for year in xrange(1901, 2001):
  for month in xrange(1,13):
      if calendar.weekday(year, month, 1) == calendar.SUNDAY:
        sundays += 1

print sundays

