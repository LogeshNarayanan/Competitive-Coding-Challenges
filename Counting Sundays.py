""" --------- Problem statement -----------
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
initialDate = 1
sunday =0
for year in range (1901,2001):
  month =1
  while(month <=12):
    if( (month ==1) or (month ==3) or (month ==5) or (month ==7) or (month ==8) or(month ==10) or (month ==12) ):
      initialDate += (31%7)
    elif ((month == 2)):
      initialDate += (28%7)
      if(((year % 400 ) == 0) and (year % 100 ) != 0) or ((year % 4 ) == 0):
        initialDate +=1
    else:
      initialDate += (30%7)
    if(initialDate % 7 == 6):
      sunday +=1
    month +=1
print sunday
