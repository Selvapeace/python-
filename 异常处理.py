# 异常处理
try:
    num = eval(input("please input an integar"))
    print(num**2)
except NameError:                # 异常时执行
    print("输入不是整数")
else:                          # 无异常时执行
    print("没有异常")
finally:                    # 不管有无异常，都要执行
    print("over")
