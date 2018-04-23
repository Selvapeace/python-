temp = input()
tempnum = float(temp[1:-1] + temp[-1])
if temp[0] in ['C','c']:
    F = tempnum * 1.8 + 32
    print("F{:.2f}".format(F))
elif temp[0] in ['F','f']:
    C = (tempnum - 32) / 1.8
    print("C{:.2f}".format(C))
else:
    print('wrong')
