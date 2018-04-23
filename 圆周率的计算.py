# 数学方法求圆周率
pi = 0
N = 100       # 斜杠换行
for k in range(N):
    pi += 1/pow(16,k)*( \
        4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率的值{}".format(pi))


# 蒙特卡罗方法求圆周率
import random
import time
DARTS = 3000*3000
hits = 0.0
start = time.perf_counter()
for i in range(1,DARTS+1):
    x,y = random.random(),random.random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)        # 一共DARTS个点（四分之一圆中），计算落入圆内的点占总数的比例
print('圆周率的值是{}'.format(pi))
print('运行时间是{}s'.format(time.perf_counter()-start))
