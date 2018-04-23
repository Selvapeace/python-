# method 1
height,weight = eval(input("请输入身高（米）和体重（公斤）,逗号分隔:"))
bmi = weight / pow(height,2)
print("BMI:{:.2f}".format(bmi))
who = ''
if bmi < 18.5:
    who = '偏瘦'
elif 18.5 <= bmi < 25:
    who = '正常'
elif 25 <= bmi < 30:
    who = '偏胖'
else:
    who = '肥胖'
print("BMI指标为：国际'{0}'".format(who))
nat = ''
if bmi < 18.5:
    nat = '偏瘦'
elif 18.5 <= bmi < 24:
    nat = '正常'
elif 24 <= bmi < 28:
    nat = '偏胖'
else:
    nat = '肥胖'
print("BMI指标为：国内'{0}'".format(nat))


# method 2
height,weight = eval(input("请输入身高（米）和体重（公斤）,逗号分隔:"))
bmi = weight / pow(height,2)
print("BMI:{:.2f}".format(bmi))
who,nat = '',''
if bmi < 18.5:
    who,nat = '偏瘦','偏瘦'
elif 18.5 <= bmi < 24:
    who,nat = '正常','正常'
elif 24 <= bmi < 25:
    who,nat = '正常','偏胖'
elif 25 <= bmi < 28:
    who,nat = '偏胖','偏胖'
elif 28 <= bmi < 30:
    who,nat = '偏胖','肥胖'
else:
    who = '肥胖'
print("BMI指标为：国际{},国内'{}'".format(who,nat))
