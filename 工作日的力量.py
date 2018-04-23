# 工作日的力量
dayfactor = 0.01
dayup = 1     # 基础
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("每周5个工作日每天进步{}，双休日每天退步{}，则一年后变为一年前的{:.2f}倍：".format(dayfactor,dayfactor,dayup))
