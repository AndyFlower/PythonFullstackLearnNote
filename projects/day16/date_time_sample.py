# date
import datetime
d = datetime.date(2020,10,10)
print(d) #2020-10-10
print(d.year)
print(d.month)

# time
t = datetime.time(10,10,10)
print(t) #10:10:10

# time类属性
print(t.hour)
print(t.minute)

# datetime
dt = datetime.datetime(2020,1,1,10,10,10)
print(dt) #2020-01-01 10:10:10

#datetime主要用于计算
#timedelta:时间的变化量
td = datetime.timedelta(days=1)
print(td) #1 day, 0:00:00
# 参与数值运算



