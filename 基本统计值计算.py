# 基本统计值计算

def getNum():
    nums = []
    a = input('请输入数字（回车后输入下一个数字；直接回车完成输入）：')
    while a != '':
        nums.append(eval(a))
        a = input('请输入数字（回车后输入下一个数字；直接回车完成输入）：')
    return nums

def mean(x):
    summary = 0
    for each in x:
        summary += each
    mean = summary / len(x)
    return mean

def var(x):
    add = 0
    for each in x:
        add += (each - mean(x))**2
    var = add / (len(x)-1)
    return var

def median(x):
    x = sorted(x)            # 对列表元素排序
    if len(x) % 2 == 0:
        median = ( x[int(len(x)/2 - 1)] + x[int(len(x)/2)] ) / 2
    else:
        median = x[int((len(x)-1)/2)]
    return median

m = getNum()
print('均值{}，方差{}，中位数{}'.format(mean(m),var(m),median(m)))
