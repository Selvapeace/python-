# 连续打印进度条
import time
scale = 10
print('----------执行开始-----------')
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print('----------执行结束-----------')



# 进度条的刷新
# 两个问题：1、每次print不能换行；2、每次print完光标回到开头
import time
for i in range(101):
    print("\r{:3}%".format(i),end = '')
    time.sleep(0.1)
# 在IDLE中看不出效果，因为/r的功能在IDLE不能用
# 在cmd中输入“路径\python 文件名.py” 即可运行


import time
scale = 50
start = time.perf_counter()
print('执行开始'.center(scale//2,'-'))
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = '')
    time.sleep(0.1)
print('\n' + '执行结束'.center(scale//2,'-'))
