Tempstr = input("请输入带有符号的温度值：")
if Tempstr[-1] in ['F','f']:     # 最后一个字符是-1，倒数第二个是-2，以此类推
    C = (eval(Tempstr[0:-1]) - 32 )/1.8    # [0:-1]指倒数第0个字符开始，不到倒数第1个字符，也即删除倒数第1个字符
    print("转换后的温度是{:2f}C".format(C))
elif Tempstr[-1] in ['C','c']:
    F = 1.8 * eval(Tempstr[0:-1]) + 32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print("输入格式错误")
