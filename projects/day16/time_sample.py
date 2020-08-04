import time

# 获取时间戳
print(time.time()) #1596415177.0463836

# 格式化时间对象
print(time.gmtime()) #time.struct_time(tm_year=2020, tm_mon=8, tm_mday=3, tm_hour=0, tm_min=44, tm_sec=1, tm_wday=0, tm_yday=216, tm_isdst=0)
print(time.localtime()) #time.struct_time(tm_year=2020, tm_mon=8, tm_mday=3, tm_hour=8, tm_min=45, tm_sec=18, tm_wday=0, tm_yday=216, tm_isdst=0)

# 格式化时间对象和字符串之间的转换

s = time.strftime("%Y/%m/%d %H:%M:%S") #2020/08/03 08:50:44
print(s)

# 时间字符串转换为时间对象
s = time.strptime('2020 05 20','%Y %m %d') #time.struct_time(tm_year=2020, tm_mon=5, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=141, tm_isdst=-1)
print(s)

# 时间对象->时间戳
t1 = time.localtime() # 时间对象
t2 = time.mktime(t1) # 时间戳
print(t2)

# 线程暂停
time.sleep(3)