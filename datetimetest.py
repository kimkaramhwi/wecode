import datetime # 모듈이름과 파이썬 파일이름이 같으면 오류 발생

# now = datetime.datetime.now()
# print(now)  # 2022-03-22 11:39:59.578982

# nowDate = now.strftime('%Y-%m-%d')
# print(nowDate)  # 2022-03-22

# nowTime = now.strftime('%H:%M:%S')
# print(nowTime)  # 11:39:59

# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# print(nowDatetime)  # 2022-03-22 11:39:59

# timeStr = '2022-03-23 09:18:33'
# Thistime = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')

# print(type(Thistime))  # <class 'datetime.datetime'>
# print(Thistime)  # 2022-03-23 09:18:33

# myDatetime = datetime.datetime.strptime('2022-03-23 09:18:33', '%Y-%m-%d %H:%M:%S')

# yourDatetime = myDatetime.replace(day=27)
# print(myDatetime)  # 2022-03-23 09:18:33
# print(yourDatetime)  # 2022-03-27 09:18:33

# d = datetime.date(2022, 3, 23)
# t = datetime.time(9, 18, 33)

# dt = datetime.datetime.combine(d, t)
# print(dt)  # 2022-03-23 09:18:33

# now = datetime.datetime.now()
# nowTuple = now.timetuple()
# print(nowTuple)
# # time.struct_time(tm_year=2022, tm_mon=3, tm_mday=23, tm_hour=10, tm_min=11, tm_sec=50, tm_wday=2, tm_yday=82, tm_isdst=-1)
# print(nowTuple.tm_year)  # 2022
# print(nowTuple.tm_wday)  # 2
# print(nowTuple.tm_mday)  # 23

# now = datetime.datetime.now()
# print(now)  # 2022-03-23 10:14:48.929526

# tomorrow = now + datetime.timedelta(days=1)
# print(tomorrow)  # 2022-03-24 10:14:48.929526

a_Datetime = datetime.datetime.strptime('2022-03-23 00:00:10', '%Y-%m-%d %H:%M:%S')
b_Datetime = datetime.datetime.strptime('2022-03-22 00:00:00', '%Y-%m-%d %H:%M:%S')
result = a_Datetime - b_Datetime

print(result)  # 1 day, 0:00:10
print(result.days)  # 1
print(result.seconds)  # 10
