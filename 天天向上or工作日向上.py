# 只在工作日努力到什么程度，才能与每天努力1%一样呢？
# my method
dayfactor = 0.01
dayup = 1
daydayup = pow(1 + 0.01,365)
while dayup < daydayup:
    dayfactor += 0.001
    for i in range (365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + dayfactor)    # 这里错了！会导致每次乘的dayfactor不一样！
print("只在工作日努力则需要日均进步{:5f}，才能与每天努力1%一样".format(dayfactor))


# teacher's method
def dayUP(df):      # 定义函数
    dayup = 1
    for i in range (365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup          # 这样函数输出的是dayup，而df在整个函数中是固定值
dayfactor = 0.01
while dayUP(dayfactor) < pow(1 + 0.01,365):
    dayfactor += 0.001
print("只在工作日努力则需要日均进步{:5f}，才能与每天努力1%一样".format(dayfactor))
