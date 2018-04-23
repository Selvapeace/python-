# 函数递归：函数定义中调用函数自身,递归存在链条（递归表达式）和基例（停止递归的点）
# 用分支语句来区分链条和基例
# 递归是数学归纳法思维在编程中的体现

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# example 1 字符串反转（也可用s[::-1])
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]

# example 2 斐波那契数列
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) +  f(n-2)

# example 3 汉诺塔问题
count = 0      # n是搬运圆环的个数/编号，src是初始圆柱，dst是目标圆柱，mid是辅助圆柱
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)       # 把上n-1个圆环先搬到中间圆柱
        print('{}:{}->{}'.format(n,src,dst))   # 再把第n个圆环放到目标圆柱
        count += 1
        hanoi(n-1,mid,dst,src)      # 最后把中间圆柱上的n-1个圆环放到目标圆柱
