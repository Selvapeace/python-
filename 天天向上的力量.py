# 每天都进步or退步
dayfactor = 0.01
dayup = pow(1 + dayfactor,365)
daydown = pow(1 - dayfactor,365)
print("每天进步：{}，向上：{:.2f}，向下：{:.2f}".format(dayfactor,dayup,daydown))
