today_utc = 'Tuesday'
time_utc = 10.30
timezone = int(input())
if timezone + time_utc < 0:
    print('Monday')
elif 0 < timezone + time_utc < 24:
    print('Tuesday')
elif 0 < timezone + time_utc >= 24:
    print('Wednesday')
