import time

# 时间获取
time.time()   # 浮点
time.ctime()    # 易理解的格式
time.gmtime()   # 其他程序可用的格式

# 时间格式化
time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
  # 其他：%B 月份名称； %b 月份名称的缩写； %A 星期； %a 星期缩写；%h 12小时制；%p 上下午
timestr = '2018-04-02 01:03:34'
time.strptime(timestr,"%Y-%m-%d %H:%M:%S")    # 把字符串变成计算机可操作的时间


## 程序计时
start = time.perf_counter()
end = time.perf_counter()
end - start

time.sleep(3)    # 让程序休眠3秒
def wait():
    time.sleep(3)
wait()              # wait() 让程序停3秒后退出

